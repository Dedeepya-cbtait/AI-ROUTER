def analyze_sentiment(input_text: str):
    text = input_text.lower()

    positive_words = ["good", "happy", "great", "awesome"]
    negative_words = ["bad", "sad", "terrible", "angry"]

    if any(word in text for word in positive_words):
        return "Positive"
    elif any(word in text for word in negative_words):
        return "Negative"
    else:
        return "Neutral"