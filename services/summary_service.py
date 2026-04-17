def summarize_text(input_text: str):
    words = input_text.split()
    return " ".join(words[:5]) + "..." if len(words) > 5 else input_text