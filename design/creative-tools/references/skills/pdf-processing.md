---
name: "pdf-processing"
title: "PDF Processing"
description: "Use for processing PDF documents programmatically using Python (pypdf, pdfplumber, reportlab) and CLI tools (qpdf, pdftk) for merging, splitting, extraction, form filling, OCR, and creation."
risk: "safe"
source: "https://github.com/ilucomutcnas/arcana-skills"
date_added: "30.03.2026"
---

## Package Structure

- Main router: `SKILL.md`
- This reference: `references/skills/pdf-processing.md`
- Examples: `examples/skills/pdf-processing.md`
- Forms guide: `pdf-processing__references/forms.md`
- Full reference: `pdf-processing__references/reference.md`
- License: `pdf-processing__references/LICENSE.txt`
- Scripts: `pdf-processing__scripts/` (7 Python scripts for form handling and validation)

## Linked Package Files

- Adjacent: `references/skills/content-creator.md` — for content that goes into PDFs
- Validation: `pdf-processing__references/forms.md` — for form filling instructions

## Purpose

Process PDF documents using Python libraries and command-line tools. Covers merging, splitting, text extraction, table extraction, PDF creation, form filling, watermarking, password protection, OCR for scanned documents, and metadata extraction.

For form filling, read `pdf-processing__references/forms.md` and follow its instructions.
For advanced features and JavaScript libraries, see `pdf-processing__references/reference.md`.

## When to Use

- When merging or splitting PDF files
- When extracting text, tables, or images from PDFs
- When creating new PDFs from scratch
- When filling PDF forms programmatically
- When adding watermarks or password protection
- When OCR-scanning scanned PDFs for searchable text
- When extracting or modifying PDF metadata

## Workflow

1. Identify the task type (merge, split, extract, create, fill, watermark, encrypt, OCR).
2. Choose the appropriate tool:
   - pypdf: merge, split, rotate, metadata, encrypt, watermark
   - pdfplumber: text extraction with layout, table extraction
   - reportlab: create PDFs from scratch (Canvas or Platypus)
   - pytesseract + pdf2image: OCR scanned PDFs
   - qpdf/pdftk: command-line operations
3. For form filling, follow `pdf-processing__references/forms.md` instructions.
4. Validate output.

## Quality Standards

- Always verify output PDF is readable and uncorrupted.
- Preserve page order and orientation when merging or splitting.
- Handle errors gracefully (missing files, password-protected PDFs, corrupted files).
- Dispose of temporary files after processing.

## Technical Rules

Python libraries:
- `pypdf`: basic operations (merge, split, rotate, metadata, encrypt, watermark).
- `pdfplumber`: text extraction with layout, table extraction to DataFrame.
- `reportlab`: PDF creation (Canvas for precise layout, Platypus for document flow).
- `pytesseract` + `pdf2image`: OCR for scanned PDFs.

CLI tools:
- `qpdf`: merge, split, rotate, decrypt from command line.
- `pdftk`: merge, split, rotate, burst from command line.
- `pdftotext` (poppler-utils): text extraction from command line.
- `pdfimages` (poppler-utils): image extraction.

Quick reference:

| Task | Best Tool |
|------|-----------|
| Merge PDFs | pypdf or qpdf |
| Split PDFs | pypdf or qpdf |
| Extract text | pdfplumber |
| Extract tables | pdfplumber |
| Create PDFs | reportlab |
| OCR scanned PDFs | pytesseract + pdf2image |
| Fill PDF forms | see forms.md |
| Command-line operations | qpdf or pdftk |

## Validation

- Verify output PDF opens correctly.
- Confirm page count matches expectations.
- Check extracted text or tables for completeness.
- Validate form fields are filled correctly.

## Restrictions

- Do not use deprecated libraries.
- Do not skip error handling for file operations.
- For form filling, always follow `pdf-processing__references/forms.md` — do not improvise.

## Output Requirements

- Processed PDF files.
- Extracted text or tables in requested format.
- Error reports for any processing failures.
