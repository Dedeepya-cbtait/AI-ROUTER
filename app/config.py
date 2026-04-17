def load_config():
    return {
        "text": "app.services.text_service.process_text",
        "sentiment": "app.services.sentiment_service.analyze_sentiment",
        "summary": "app.services.summary_service.summarize_text"
    }