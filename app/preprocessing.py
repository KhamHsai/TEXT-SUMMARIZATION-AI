import re

def clean_text(text: str) -> str:
    """
    Clean the input text by removing extra spaces,
    line breaks, and tab spaces.
    """
    if not text:
        return ""
    
    # Replace line breaks and tab spaces with a single space
    # \n = newline, \r = carriage return, \t = tab
    text = re.sub(r"[\n\r\t]+", " ", text)
    
    # Remove multiple spaces and trim the ends
    text = re.sub(r"\s+", " ", text).strip()
    return text

def truncate_text(text: str, max_words: int = 500) -> str:
    """
    Truncate the text if it is longer than max_words.
    """
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words])

def preprocess_text(text: str, max_words: int = 500) -> str:
    """
    Full preprocessing pipeline:
    1. Clean the text
    2. Truncate the text
    """
    text = clean_text(text)
    text = truncate_text(text, max_words=max_words)
    return text

if __name__ == "__main__":
    # Task 3: Test with the standard sample
    sample_text = "AI is growing fast.\n\nIt helps in\teducation, healthcare, and business."
    
    # Class Activity: Use the 'MESSY' text for your screenshot!
    # activity_text = "aI Is GrOwInG FaSt.\nIt HELPS in Education, HEALTHCARE, and business."
    
    processed = preprocess_text(sample_text, max_words=20)
    print("\n--- Processed Text ---")
    print(processed)
    print("----------------------\n")