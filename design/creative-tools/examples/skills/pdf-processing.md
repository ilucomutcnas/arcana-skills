# PDF Processing — Examples

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Merge PDFs

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

## Extract Tables

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

if all_tables:
    combined_df = pd.concat(all_tables, ignore_index=True)
    combined_df.to_excel("extracted_tables.xlsx", index=False)
```

## CLI Tools

```bash
# Merge with qpdf
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Extract text preserving layout
pdftotext -layout input.pdf output.txt

# Extract images
pdfimages -j input.pdf output_prefix
```

## Quick Reference

| Task | Best Tool | Key Command |
|------|-----------|-------------|
| Merge | pypdf | `writer.add_page(page)` |
| Split | pypdf | One page per file |
| Extract text | pdfplumber | `page.extract_text()` |
| Extract tables | pdfplumber | `page.extract_tables()` |
| Create | reportlab | Canvas or Platypus |
| OCR scanned | pytesseract | Convert to image first |
| Fill forms | see forms.md | Follow forms.md |
| CLI merge | qpdf | `qpdf --empty --pages ...` |

For form filling instructions, see `pdf-processing__references/forms.md`.
For advanced features and JavaScript libraries, see `pdf-processing__references/reference.md`.
