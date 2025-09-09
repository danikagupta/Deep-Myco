# Myco Papers Pipeline (Folder-Scoped)

This folder contains a **self-contained pipeline** that turns raw PDFs into structured experimental data using a sequence of Streamlit- and Python-based steps:
1) **Ingest PDFs** → 2) **Extract text** → 3) **Classify (multi-stage)** → 4) **Compute metrics** → 5) **Dedupe** → 6) **Extract experimental tables** → 7) **Combine tables** → 8) **(Optional) Crawl references to fetch more PDFs**

> This README is designed for a public GitHub repo *without moving files* (Step 1). It assumes everything lives in **one folder** inside a larger repository.

---

## Quickstart

### 1) Requirements
- Python 3.10+
- (Optional) Make
- OpenAI & Serpstack API keys (if you’ll run LLM stages or the reference crawler)

### 2) Install
```bash
cd <this-folder>  # e.g., tools/myco_pipeline
python -m venv .venv && . .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### 3) Configure secrets
Copy `.env.example` to `.env` and fill in values.
```bash
cp .env.example .env
# then edit .env
```

**Environment variables**
```bash
OPENAI_API_KEY=            # required for LLM-based classification/extraction
SERPSTACK_API_KEY=         # required to crawl for PDF links by reference
MYCO_DATA_DIR=./data       # where working files and outputs go
OPENAI_MODEL=gpt-4o-mini
MAX_INPUT_TOKENS=100000
```

### 4) Prepare data workspace
This folder uses a runtime workspace under `MYCO_DATA_DIR`. You can pre-create the directories or let scripts create them as needed.

```bash
python -c "from io_paths import ensure_dirs; ensure_dirs(); print('data workspace ready')"
```

### 5) Run something
All scripts can be executed directly (Streamlit ones open a local UI). Examples:
```bash
# Upload PDFs via UI
streamlit run upload_files.py

# Extract text from PDFs → pdf_txt/*.txt
streamlit run extract_pdf_text.py

# Stage 1 classification (relevance scoring)
streamlit run process_classify.py

# Extract experimental tables (2025 schema) for selected papers
streamlit run process_extract_2025_1.py

# Combine extracted tables
streamlit run process_extract_2025_2.py
```

> Tip: You can also run non-Streamlit scripts directly with `python <script>.py` if they don’t rely on a UI.

---

## Data folders (runtime)

All data is stored under `MYCO_DATA_DIR` (defaults to `./data`), which is **git-ignored**. Subfolders are created on demand:

```
data/
  raw_pdf/           # intake PDFs
  processed_pdf/     # successfully handled PDFs
  error_pdf/         # errored PDFs
  pdf_txt/           # extracted txt from PDFs
  pdf_pages/         # per-page PNGs (vision stages)
  pdf_tables/        # extracted experiment tables (v1)
  pdf_tables_2025/   # extracted experiment tables (2025 schema)
  raw_references/    # per-reference JSON rows
  downloaded_ref/    # reference JSONs whose PDFs were successfully fetched
  errored_ref/       # reference JSONs that failed to fetch
  outputs/           # combined CSVs (pdf_text.csv, pdf_extract.csv, pdf_extract_2025.csv)
```

---

## Pipeline overview

### A) Ingest & text extraction
- **`upload_files.py`** — Streamlit uploader that writes PDFs to `raw_pdf/`.
- **`extract_pdf_text.py`** — Reads PDFs → writes text files to `pdf_txt/` (skips existing, shows progress).

### B) Multi-stage classification & metrics
These scripts operate over `pdf_txt/*.txt` and maintain a master CSV `outputs/pdf_text.csv` with a **`status`** column that advances through stages to avoid double-processing.

1. **`process_classify.py`** — Stage 1: score (1–10) for *mycoremediation* relevance (adds `score`, `comments`, sets `status=processed`).
2. **`process_classify2.py`** — Stage 2: “experimental mycoremediation?” focus score (adds `score2`, `comments2`, `status=processed2`).
3. **`process_classify3.py`** — Stage 3: fungi used for dye remediation? **YES/NO** (adds `fungi`, `reason`, `status=processed3`).
4. **`process_data4.py`** — Stage 4: bytes/words/tokens (adds `bytes`, `words`, `tokens`, `status=processed4`).
5. **`process_classify5.py`** — Stage 5: study type (**Experimental / Summary / Neither**) (adds `study`, `studyReason`, `status=processed5`).
6. **`process_data6.py`** — Stage 6: MD5 + duplicate count (adds `md5`, `match_hash`, `status=processed6`).

### C) Experiment table extraction
- **`process_extract1.py`** — Extracts rows of experimental setups/results for **top candidates** (filters by status/scores/fungi/duplicates). Writes per-paper CSVs to `pdf_tables/`, bumps `status=processed7`.
- **`process_extract_2025_1.py`** — Updated extractor (11+ columns; includes fungi form). Reads token limits, truncates if necessary. Writes per-paper CSVs to `pdf_tables_2025/`, bumps `status=processed8`.
- **`process_extract2.py`** — Combines per-paper tables → `outputs/pdf_extract.csv` (legacy path).
- **`process_extract_2025_2.py`** — Combines per-paper tables → `outputs/pdf_extract_2025.csv` (adds `source_file`).

### D) (Optional) Reference-based crawling
- **`process_pdf.py` / `process_pdf_image.py` / `process_pdf_text.py`** — Turn a references table into per-reference JSON files in `raw_references/` either via PDF-page images (vision model) or direct text extraction.
- **`test.py`** — Testing helper to convert a pasted references table (`output.txt`) to JSON rows in `raw_references/`.
- **`process_ref.py`** — Uses **Serpstack** to search for PDF links by reference; downloads the first viable PDF into `raw_pdf/`; moves each reference JSON to `downloaded_ref/` or `errored_ref/`.

### E) Utilities
- **`stats.py`** — Simple Streamlit dashboard with counts across the working directories.

---

## Environment & secrets

- No API keys are stored in code. The pipeline reads secrets from environment variables (`.env` for local dev) or Streamlit secrets if configured.
- Keys required:
  - `OPENAI_API_KEY` for LLM classification and extraction.
  - `SERPSTACK_API_KEY` for reference crawling.
- You can also set `MYCO_DATA_DIR` to point to any writable working directory.

---

## Status field (processing guardrails)

The master CSV tracks where each file is in the pipeline to avoid re-processing:

```
new → processed → processed2 → processed3 → processed4 → processed5 → processed6 → processed7 → processed8
```

Extraction stages filter heavily (e.g., high scores, Experimental, fungi=Yes, no duplicates) before producing structured tables.

---

## Troubleshooting

- **Missing keys**: If a script requires an API key, ensure it’s set in `.env`. You can also export it in your shell:
  ```bash
  export OPENAI_API_KEY=sk-...
  export SERPSTACK_API_KEY=...
  ```
- **File not found / permission**: Ensure `MYCO_DATA_DIR` exists and is writable; run the `ensure_dirs()` step above.
- **Token limit exceeded**: The extractor will truncate text to respect `MAX_INPUT_TOKENS`. You can lower this in `.env` if needed.
- **Duplicates**: If `match_hash > 0`, the file likely duplicates previously seen content.

---

## Contributing (within the larger repo)

- Keep all logic changes incremental in this folder for now (Step 1). 
- Prefer adding new utilities to `config.py` and `io_paths.py` rather than hard-coding paths/secrets.
- When ready, we can refactor to a shared package (Step 2+).

---

## License

Add your project’s license at the repo root (e.g., MIT, Apache-2.0) and reference it here.
