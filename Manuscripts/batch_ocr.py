import os
import json
from PIL import Image
from deepseek_ocr import DeepSeekOCR

# Path to your images
IMAGE_FOLDER = "Image-Manuscripts"  # <-- change this to your folder name

# Output folder for OCR results
OUTPUT_FOLDER = "OCR_Manuscripts"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load the OCR model once
ocr = DeepSeekOCR()

# Loop through all image files
for filename in sorted(os.listdir(IMAGE_FOLDER)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):

        image_path = os.path.join(IMAGE_FOLDER, filename)
        print(f"OCR → {filename}")

        # Open the image
        img = Image.open(image_path)

        # Run OCR
        result = ocr.ocr(img)

        # Save output as JSON
        output_path = os.path.join(OUTPUT_FOLDER, f"{filename}.json")
        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)

print("Done! All images processed.")
