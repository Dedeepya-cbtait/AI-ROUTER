from pydantic import BaseModel, Field

class RequestModel(BaseModel):
    type: str = Field(..., example="text")
    input: str = Field(..., min_length=1)