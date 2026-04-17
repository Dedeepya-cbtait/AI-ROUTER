# SMART-AI-ROUTER

## INTRODUCTION
Smart AI Router is a FastAPI-based backend API that routes incoming requests to different services such as text processing, sentiment analysis, and summarization.

## FEATURES
Uppercase text conversion
Keyword-based sentiment detection
Basic text summarization    
Clean modular architecture
Swagger UI and Postman support


## SRUCTURE  OF THE PROJECT
smart-ai-router/
│
├── app/
│   ├── main.py
│   ├── router.py
│   ├── config.py
│   ├── models.py
│   ├── logger.py
│   │
│   ├── services/
│   │   ├── text_service.py
│   │   ├── sentiment_service.py
│   │   └── summary_service.py
│
├── config.json
├── requirements.txt
└── README.md

## TECH STACK
Python
FastAPI
Uvicorn
Pydantic
Postman

## INSTALLATION
cd..AI-ROUTER
pip install -r requirements.txt

## RUN SERVER
python -m uvicorn app.main:app --reload 

## OPEN API Docs:
http://127.0.0.1:8000/docs

## API
POST /process

## TEXT
REQUEST:
{
    "type":"text",
    "input":"hello ai-router"

}
RESPONSE:
{
    "type": "text",
    "result": "HELLO AI-ROUTER"
}

## SENTIMENT(POSITIVE)
REQUEST:
{
    "type":"sentiment",
    "input":"I had a great day"

}
RESPONSE:
{
    "type": "sentiment",
    "result": "Positive"
}
# NEGATIVE
REQUEST:
{
    "type":"sentiment",
    "input":"the wheather is terrible"

}
RESPONSE:
{
    "type": "sentiment",
    "result": "Negative"
}
# NEURAL
REQUEST:
{
    "type":"sentiment",
    "input":"i bought a dress"

}
RESPONSE:
{
    "type": "sentiment",
    "result": "Neutral"
}

## SUMMARY
REQUEST:
{
    "type":"summary",
    "input":"hii from ai-router"

}
RESPONSE:
{
    "type": "summary",
    "result": "HII FROM A"
}

## TESTING
Swagger UI
Postman

## CONCLUSION
The Smart AI Router project demonstrates a modular FastAPI-based backend system capable of routing different request types to dedicated services. It serves as a strong foundation for future AI-powered enhancements such as advanced NLP, deployment, and authentication.This project shows how to build an API that processes different user requests based on type. It uses FastAPI and Python to route text, sentiment, and summary requests. It helped in learning backend development, API testing, and modular coding. The project can be improved further with AI models and deployment.
