import pytesseract
from PIL import Image
import os

def extract_text(image_path):
    """
    Extract text/symbols from an image using Tesseract OCR.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"