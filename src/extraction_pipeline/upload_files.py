import streamlit as st
import os

from config import settings, require
from io_paths import (ensure_dirs, RAW_PDF, PROCESSED_PDF, ERROR_PDF, PDF_TXT, PDF_PAGES,
                      PDF_TABLES, PDF_TABLES_2025, RAW_REFS, DOWNLOADED_REF, ERRORED_REF, OUTPUTS)

ensure_dirs()
OPENAI_API_KEY = require('OPENAI_API_KEY', settings.openai_key)



def process_one_file(pdfbytes,name="Unknown"):
    output_dir = str(RAW_PDF)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path1 = os.path.join(output_dir, f'{name}')
    with open(output_path1, 'wb') as f:
        f.write(pdfbytes)
        

st.header("Upload PDF files")
uploaded_files=st.file_uploader("Upload PDF file",type="pdf", accept_multiple_files=True)
if st.button("Upload") and uploaded_files is not None:
    for uploaded_file in uploaded_files:
        process_one_file(uploaded_file.read(),uploaded_file.name)
        st.write(f"Uploaded {uploaded_file.name}")
st.divider()