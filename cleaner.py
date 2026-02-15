import pdfplumber
import re

def clean(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for pg in pdf.pages:
            text += pg.extract_text() or ""
    text = re.sub(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b', '[CARD]', text)
    text = re.sub(r'\b\d{8,12}\b', '[ACC]', text)
    return text