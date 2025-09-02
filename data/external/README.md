# Enzyme Commission Annotations (external)

This folder contains a single CSV that links fungi mentioned in our experiments to **enzyme activities** with **EC numbers** and supporting **evidence snippets**.

## Contents
- `enzyme_commission.csv` — normalized enzyme annotations extracted from experimental notes.

## Data Dictionary

| Column                 | Type   | Description                                                                                           |
|------------------------|--------|-------------------------------------------------------------------------------------------------------|
| `original_fungi_name`  | string | Fungal name exactly as it appeared in the source dataset.                                             |
| `species_name`         | string | Canonicalized species name when available (from the fungi enrichment table).                          |
| `enzyme_name`          | string | Normalized enzyme capability (controlled list below).                                                 |
| `EC_number`            | string | Enzyme Commission identifier corresponding to `enzyme_name`.                                          |
| `evidence`             | string | Short text snippet from the “any additional information” field where the enzyme term was detected.    |
| `notes`                | string | Clarifications (e.g., “Includes mediator system / LMCO” for laccase mediator system mentions).        |
| `source_file`          | string | Propagated reference to the originating file/record if present in the source data.                    |

## Controlled Vocabulary for `enzyme_name`

- **Laccase** — `EC 1.10.3.2` (includes LMCO/LMS mentions)  
- **Manganese peroxidase** — `EC 1.11.1.13`  
- **Lignin peroxidase** — `EC 1.11.1.14`  
- **Versatile peroxidase** — `EC 1.11.1.16`  
- **Dye-decolorizing peroxidase** (DyP) — `EC 1.11.1.19`  
- **Peroxidase (unspecified)** — `EC 1.11.1.7`  
- **Tyrosinase / Polyphenol oxidase** — `EC 1.14.18.1`  
- **Catalase** — `EC 1.11.1.6`  
- **Glucose oxidase** — `EC 1.1.3.4`  
- **Aryl-alcohol oxidase** — `EC 1.1.3.7`  
- **Lipoxygenase** — `EC 1.13.11.12`  
- **Triacylglycerol lipase** — `EC 3.1.1.3`  
- **Cellulose 1,4-β-cellobiosidase (Exoglucanase)** — `EC 3.2.1.91`  
- **Cellulase (Endo-1,4-β-glucanase)** — `EC 3.2.1.4`  
- **β-Glucosidase** — `EC 3.2.1.21`  
- **Endo-1,4-β-xylanase** — `EC 3.2.1.8`  
- **Xylan 1,4-β-xylosidase** — `EC 3.2.1.37`  
- **Lytic polysaccharide monooxygenase** — `EC 1.14.99.-` (family-level LPMOs; specific ECs vary)

## Quick Start (Python)

```python
import pandas as pd

df = pd.read_csv("enzyme_commission.csv")

# All fungi reported with Laccase activity
laccase_df = df[df["enzyme_name"] == "Laccase"]

# Presence/absence matrix (fungi × enzymes)
presence = (
    df.assign(value=1)
      .pivot_table(index="species_name", columns="enzyme_name", values="value", aggfunc="max", fill_value=0)
)

# Filter by EC number (MnP)
mnps = df[df["EC_number"] == "EC 1.11.1.13"]
```

## Usage Notes

- A single fungus may appear in multiple rows (one per enzyme capability).  
- The **evidence** field is a short excerpt to help manual verification; consult the source data for full context.  
- **LPMOs** are annotated at the family level (`EC 1.14.99.-`) unless a specific LPMO EC is explicit.  
- **Peroxidase (unspecified)** is used when the text mentions “peroxidase” without specifying LiP/MnP/VP.

## Known Limitations

- **Text-based detection**: Misspellings or absent enzyme names won’t be captured.  
- **Ambiguous abbreviations**: We err on the conservative side; generic “peroxidase” stays unspecified.  
- **Species normalization**: `species_name` may be blank for unresolved or non-species entries.

## TODOs

- [ ] Expand patterns to catch additional GH/AA families (e.g., **AA9 LPMO**, **GH5**, **GH10**, etc.).  
- [ ] Disambiguate generic **peroxidase** mentions where context allows.  
- [ ] Add a confidence score (e.g., exact match vs. inferred).  
- [ ] Periodically re-sync `species_name` with the latest taxonomy enrichment.

---

**License / Attribution**  
Internal research data. If sharing externally, scrub `source_file` paths as needed and attribute the originating studies.
