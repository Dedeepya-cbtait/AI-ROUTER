from fastapi import FastAPI
from app.models import RequestModel
from app.router import route_request

app = FastAPI()

@app.post("/process")
def process_request(request: RequestModel):

    result = route_request(request.type, request.input)

    return result