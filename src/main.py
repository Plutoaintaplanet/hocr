import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from hocr.src.ocr import extract_text
from hocr.src.translate import translate_hieroglyphs

def run(image_path):
    """
    Main pipeline: Load image -> Extract text -> Translate
    """
    print("="*50)
    print("🔍 ROSETTA STONE AI TRANSLATOR")
    print("="*50)
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"❌ Error: Image not found at {image_path}")
        return
    
    print(f"\n📷 Loading image: {image_path}")
    
    # Step 1: Extract text
    print("\n🔎 Extracting text from image...")
    raw_text = extract_text(image_path)
    print(f"Extracted: {raw_text[:200]}")
    
    # Step 2: Translate
    print("\n🌍 Translating hieroglyphs...")
    translated = translate_hieroglyphs(raw_text)
    print(f"\n✅ TRANSLATION:\n{translated}")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    test_image = "hocr/data/raw/test.png"
    
    if len(sys.argv) > 1:
        test_image = sys.argv[1]
    
    run(test_image)