from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    prompt: str
    temperature: float
    max_tokens: int

class QueryResponse(BaseModel):
    response: str
    sources: list
    usage: dict