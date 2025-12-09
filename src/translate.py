# Expanded hieroglyph dictionary
HIERO_DICT = {
    # Basic symbols
    "𓀀": "man",
    "𓀁": "seated man",
    "𓁐": "king",
    "𓂀": "eye",
    "𓃀": "foot",
    "𓄿": "arm",
    "𓇋": "reed",
    "𓏏": "bread",
    "𓊹": "god",
    "𓇳": "sun",
    "𓈖": "water",
    "𓉐": "house",
    "𓊽": "well",
    "𓋴": "folded cloth",
    "𓌙": "basket",
    "𓍯": "papyrus roll",
}

def translate_hieroglyphs(text):
    """
    Translate hieroglyphic symbols to English words.
    Returns both known and unknown symbols.
    """
    if not text:
        return "[No text to translate]"
    
    result = []
    unknown_count = 0
    
    for char in text:
        if char in HIERO_DICT:
            result.append(HIERO_DICT[char])
        elif char.strip():  # Skip whitespace
            result.append(f"[?{char}]")
            unknown_count += 1
    
    translation = " ".join(result)
    
    if unknown_count > 0:
        translation += f"\n\n({unknown_count} unknown symbols found)"
    
    return translation if translation else "[No recognizable hieroglyphs]"