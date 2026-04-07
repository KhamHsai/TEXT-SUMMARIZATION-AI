import re

def clean_text(text: str) -> str:
    """
    Clean the input text by removing extra spaces,
    line breaks, and tab spaces.
    """
    if not text:
        return ""

    # Replace line breaks and tab spaces with a single space
    text = re.sub(r"[\n\r\t]+", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text
