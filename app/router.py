def route_request(request_type, input_text):

    if request_type == "text":
        return {
            "type": "text",
            "result": input_text.upper()
        }

    elif request_type == "sentiment":
        text = input_text.lower()

        positive_words = ["good", "happy", "great", "awesome", "love", "excellent"]
        negative_words = ["bad", "sad", "angry", "terrible", "hate", "worst"]

        if any(word in text for word in positive_words):
            sentiment = "Positive"

        elif any(word in text for word in negative_words):
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        return {
            "type": "sentiment",
            "result": sentiment
        }

    elif request_type == "summary":
        return {
            "type": "summary",
            "result": input_text[:10].upper()
        }

    else:
        return {
            "error": "Invalid type"
        }