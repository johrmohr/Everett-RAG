import os
from pdf2image import convert_from_path
from tqdm import tqdm

# Folders
INPUT_FOLDER = "PDF-Manuscripts"              # <-- change if your folder name is different
OUTPUT_FOLDER = "Image-Manuscripts"           # will be created automatically

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Find all PDFs (any name)
pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

print(f"Found {len(pdf_files)} PDF files.")

for pdf_name in tqdm(pdf_files, desc="Converting PDFs"):
    pdf_path = os.path.join(INPUT_FOLDER, pdf_name)

    # Use base filename (without .pdf) for image names
    base = os.path.splitext(pdf_name)[0]

    # Convert each page
    try:
        pages = convert_from_path(pdf_path, dpi=300)  # 300 DPI for good OCR
    except Exception as e:
        print(f"ERROR converting {pdf_name}: {e}")
        continue

    for i, page in enumerate(pages):
        out_name = f"{base}_page_{i+1}.png"
        out_path = os.path.join(OUTPUT_FOLDER, out_name)
        page.save(out_path, "PNG")
