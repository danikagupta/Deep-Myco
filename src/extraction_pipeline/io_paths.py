from pathlib import Path
from config import settings

BASE = Path(settings.data_dir)

RAW_PDF        = BASE / "raw_pdf"
PROCESSED_PDF  = BASE / "processed_pdf"
ERROR_PDF      = BASE / "error_pdf"
PDF_TXT        = BASE / "pdf_txt"
PDF_PAGES      = BASE / "pdf_pages"
PDF_TABLES     = BASE / "pdf_tables"
PDF_TABLES_2025= BASE / "pdf_tables_2025"
RAW_REFS       = BASE / "raw_references"
DOWNLOADED_REF = BASE / "downloaded_ref"
ERRORED_REF    = BASE / "errored_ref"
OUTPUTS        = BASE / "outputs"

def ensure_dirs():
    for p in [RAW_PDF, PROCESSED_PDF, ERROR_PDF, PDF_TXT, PDF_PAGES,
              PDF_TABLES, PDF_TABLES_2025, RAW_REFS, DOWNLOADED_REF,
              ERRORED_REF, OUTPUTS]:
        p.mkdir(parents=True, exist_ok=True)
