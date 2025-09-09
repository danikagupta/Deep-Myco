# Myco Pipeline — Scripts Overview & Runbook

This document explains **all 18 scripts** in this folder, how they fit together, which ones are core vs. optional vs. legacy, and how to run the full pipeline end‑to‑end. You said you’ll **keep them all**—great. This guide shows how they coexist cleanly.

---

## TL;DR (what to run, in order)

**Core 2025 pipeline (recommended):**
1. `extract_pdf_text.py` → PDF → TXT
2. `process_classify.py` → Stage 1 relevance
3. `process_classify2.py` → Stage 2 experimental focus
4. `process_classify3.py` → Stage 3 fungi usage (Yes/No)
5. `process_data4.py` → bytes/words/tokens
6. `process_classify5.py` → study type (Experimental/Summary/Neither)
7. `process_data6.py` → MD5 & duplicate detection
8. `process_extract_2025_1.py` → extract experiment tables (2025 schema)
9. `process_extract_2025_2.py` → combine into one CSV (2025 schema)

**Optional features you can use any time:**
- `upload_files.py` — Streamlit uploader for PDFs
- `stats.py` — simple dashboard of folder counts
- **Reference crawler (to auto-fetch PDFs):** choose a parser (`process_pdf_text.py` OR `process_pdf.py`/`process_pdf_image.py`), then run `process_ref.py`

**Legacy (kept for completeness, not required if you use 2025 path):**
- `process_extract1.py`, `process_extract2.py`

---

## Data & config

- Runtime data lives under **`./data`** by default (configurable via `MYCO_DATA_DIR`).
- Key directories:
  - `data/raw_pdf/` (input PDFs), `data/pdf_txt/` (extracted text), `data/pdf_pages/` (page images)
  - `data/pdf_tables/` (legacy extracted tables), `data/pdf_tables_2025/` (2025 tables)
  - `data/outputs/` (combined CSVs such as `pdf_text.csv`, `pdf_extract_2025.csv`)
  - `data/raw_references/`, `data/downloaded_ref/`, `data/errored_ref/` (reference-crawler workflow)
- Config files you already added:
  - `.env.example` → copy to `.env` and fill secrets
  - `config.py`, `io_paths.py`, `.gitignore`, `requirements.txt`, `.editorconfig`, `.streamlit/secrets.toml.example`

**Environment variables:**
```
OPENAI_API_KEY=            # LLM stages
SERPSTACK_API_KEY=         # crawler
MYCO_DATA_DIR=./data
OPENAI_MODEL=gpt-4o-mini
MAX_INPUT_TOKENS=100000
```

---

## Status lifecycle (how files progress)

The master CSV (saved at `data/outputs/pdf_text.csv`) tracks a **status** for each item to prevent re-processing:

```
new → processed → processed2 → processed3 → processed4 → processed5 → processed6 → processed7 → processed8
```

- `extract_pdf_text.py`: creates `.txt` files; does not set a status
- `process_classify.py`: sets `processed`
- `process_classify2.py`: sets `processed2`
- `process_classify3.py`: sets `processed3`
- `process_data4.py`: sets `processed4`
- `process_classify5.py`: sets `processed5`
- `process_data6.py`: sets `processed6`
- `process_extract1.py` (legacy): sets `processed7`
- `process_extract_2025_1.py`: reads candidates, writes tables, sets `processed8`

> Extractors filter heavily (scores, fungi=Yes, Experimental, non-duplicate) before generating rows.

---

## Script-by-script reference

### Core extraction & classification

**`extract_pdf_text.py`**  
- **Role:** Extract text from PDFs (`raw_pdf/` → `pdf_txt/`) using PyPDF2; Streamlit UI with progress.  
- **Inputs:** `data/raw_pdf/*.pdf`  
- **Outputs:** `data/pdf_txt/<name>.txt`

**`process_classify.py` (Stage 1)**  
- **Role:** Score 1–10 for *mycoremediation* relevance; stores `score`, `comments`, sets `status=processed`.  
- **Inputs:** `data/pdf_txt/*.txt`, `data/outputs/pdf_text.csv`  
- **Outputs:** updates `data/outputs/pdf_text.csv`

**`process_classify2.py` (Stage 2)**  
- **Role:** Is it about **experimental mycoremediation**? Adds `score2`, `comments2`, sets `status=processed2`.  
- **Inputs/Outputs:** updates same CSV.

**`process_classify3.py` (Stage 3)**  
- **Role:** **Fungi used for dye remediation?** YES/NO; adds `fungi`, `reason`, sets `status=processed3`.

**`process_data4.py` (Stage 4)**  
- **Role:** File metrics: bytes/words/tokens (via `tiktoken`); sets `status=processed4`.

**`process_classify5.py` (Stage 5)**  
- **Role:** Study type: **Experimental / Summary / Neither**; adds `study`, `studyReason`, sets `status=processed5`.

**`process_data6.py` (Stage 6)**  
- **Role:** MD5 hash + duplicate count; adds `md5`, `match_hash`, sets `status=processed6`.

**`process_extract_2025_1.py`**  
- **Role:** Extract experiment tables with the **2025 schema** (11+ columns incl. fungi form). Handles token truncation. Sets `status=processed8`.  
- **Inputs:** filters on previous stages (e.g., high scores, fungi=Yes, Experimental, non-duplicate).  
- **Outputs:** per-paper CSVs in `data/pdf_tables_2025/`

**`process_extract_2025_2.py`**  
- **Role:** Combine per-paper tables into **`data/outputs/pdf_extract_2025.csv`** (adds `source_file`).

### Optional helpers

**`upload_files.py`**  
- **Role:** Streamlit uploader to put PDFs into `data/raw_pdf/`.

**`stats.py`**  
- **Role:** Quick directory counts dashboard for sanity checks.

### Reference parsing & crawling (optional)

**Choose a parser** that turns a references table into JSON rows in `data/raw_references/`:
- **`process_pdf_text.py`** — text-based parsing (reads the PDF text directly)
- **`process_pdf.py` / `process_pdf_image.py`** — image/vision parsing (converts pages to PNG and uses a vision model)

**`test.py`**  
- **Role:** Dev helper that converts a pasted references table (`output.txt`) to JSON rows, for quick tests.

**`process_ref.py`**  
- **Role:** Web **crawler/downloader**. Reads each ref JSON, searches via **Serpstack** for matching PDFs, downloads the first viable PDF into `data/raw_pdf/`, then moves ref JSON to `downloaded_ref/` or `errored_ref/`.  
- **Note:** By default it doesn’t deeply validate. If you need verification, add a title/DOI check before accepting.

### Legacy extraction (kept for completeness)

**`process_extract1.py`**  
- **Role:** Older extractor (pre-2025 schema) → outputs in `data/pdf_tables/`; sets `status=processed7`.

**`process_extract2.py`**  
- **Role:** Older combiner → `data/outputs/pdf_extract.csv`.

---

## Choosing between variants (keep all, use one at a time)

- **Extractor:** Prefer **2025** (`process_extract_2025_1.py` + `_2025_2.py`). Keep legacy for reference, but don’t run both on the same dataset unless you intend to compare schemas.
- **Reference parser:** Pick **one** for a given run:
  - `process_pdf_text.py` (text-only) **or**
  - `process_pdf.py` / `process_pdf_image.py` (vision; only one is needed).

---

## Typical run commands

```bash
# 0) Ensure data workspace exists
python -c "from io_paths import ensure_dirs; ensure_dirs(); print('ok')"

# 1) Upload or place PDFs into ./data/raw_pdf

# 2) Extract text
streamlit run extract_pdf_text.py

# 3) Run stages 1–6
streamlit run process_classify.py
streamlit run process_classify2.py
streamlit run process_classify3.py
streamlit run process_data4.py
streamlit run process_classify5.py
streamlit run process_data6.py

# 4) Extract experiment tables (2025) and combine
streamlit run process_extract_2025_1.py
streamlit run process_extract_2025_2.py
```

**Optional: crawler**
```bash
# choose a parser (text OR image) to generate raw_references/*.txt
streamlit run process_pdf_text.py      # OR
streamlit run process_pdf.py           # OR
streamlit run process_pdf_image.py

# fetch PDFs from references
streamlit run process_ref.py
```

---

## Troubleshooting & tips

- **Hidden files:** `.env` and `.env.example` are dotfiles; some file browsers hide them by default.
- **Missing API keys:** LLM and crawler steps require keys. Set in `.env` or shell env.  
- **Token limit:** `MAX_INPUT_TOKENS` guards extraction—long texts are truncated proportionally.
- **Duplicates:** If `match_hash > 0`, the file content duplicates a previous text—useful to filter before extraction.
- **Statuses not advancing:** Ensure you’re running scripts in order; each script filters by the previous status.

---

## Glossary of key CSV columns

- `score` — Stage 1 relevance (1–10), `comments` (reason)
- `score2` — Stage 2 experimental focus (1–10), `comments2` (reason)
- `fungi` — Stage 3 YES/NO (fungi used for dye remediation), `reason`
- `bytes`, `words`, `tokens` — Stage 4 size/metrics
- `study`, `studyReason` — Stage 5 study type
- `md5`, `match_hash` — Stage 6 dedupe metrics
- `status` — lifecycle marker (`processed` … `processed8`)

---

## Safety notes

- Secrets are **not** committed; the code reads keys from env (`config.py`).
- The crawler (`process_ref.py`) downloads the **first viable PDF**; consider adding a title/DOI check if accuracy matters.

---


All 18 scripts are organized so you can:
- Run the **2025** path normally,
- Keep **legacy** scripts for comparison/history,
- Use **crawler & parsers** when you want to expand your corpus.

