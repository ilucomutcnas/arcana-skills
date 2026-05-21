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

## Stage 3.8 Example: Branded PDF One-Pager/Form QA Pass

### Deliverable Context
Release package includes:
- `partner-onepager-v3.pdf` (marketing one-pager, 4 pages).
- `partner-intake-form-v2.pdf` (fillable form for channel partners).

### Script Output Evidence
| Check | Script/Method | Result | Evidence artifact |
|---|---|---|---|
| Fillable fields completeness | `check_fillable_fields.py` | 14/14 required fields present | `logs/form-fields.txt` |
| Bounding box validation | `check_bounding_boxes.py` | 0 overflow violations | `logs/bounding-boxes.json` |
| Page count integrity | `pypdf len(reader.pages)` | Expected 4 + 2 pages | `logs/page-count.txt` |
| Metadata verification | `PdfReader().metadata` | Title/author/version set | `logs/metadata.txt` |
| Text extraction/accessibility | `pdftotext -layout` | Headings/body extracted without corruption | `logs/text-extraction.txt` |

### Issue Table
| ID | Severity | Owner | Issue | Fix |
|---|---|---|---|---|
| PDF-04 | Blocker | Doc ops | Missing required “Offer terms apply” footer on page 2 | Added legal footer and regenerated v3 |
| PDF-07 | Major | Design ops | Form checkbox labels clipped in mobile view | Increased label box width and reran bounding-box check |
| PDF-09 | Minor | Marketing ops | Metadata keywords stale from v2 | Updated metadata and archived old export |

### Acceptance Criteria
- [x] All mandatory form fields validated and writable.
- [x] No text overflow in branded layout regions.
- [x] Page order and page count match approved brief.
- [x] Metadata and provenance watermark match release version.
- [x] Text extraction output is readable for accessibility review.

### Evidence Pack Summary
Delivered to `creative-qa-gate-automation`: script logs, before/after PDF hashes, issue resolution log, legal signoff note, and final acceptance checklist.
