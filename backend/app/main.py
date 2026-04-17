from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.services.bm25_service import BM25Service
from app.services.prompt_service import build_prompt
from app.services.llm_service import call_llm
from app.utils.logger import logger
from app.config import BM25_THRESHOLD
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

bm25_service = BM25Service("app/data/policies.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],  # VERY IMPORTANT
    allow_headers=["*"],
)
@app.post("/query", response_model=QueryResponse)
def handle_query(request: QueryRequest):

    query = request.query
    user_prompt = request.prompt
    temperature = request.temperature
    max_tokens = request.max_tokens

    # Step 1: Retrieve docs
    docs = bm25_service.retrieve(query)

    # Step 2: Fallback check
    if not docs or docs[0]["score"] < BM25_THRESHOLD:
        return {
            "response": "Please escalate this issue to a human support agent.",
            "sources": [],
            "usage": {}
        }

    # Step 3: Inject context into user prompt
    context = "\n\n".join([d["content"] for d in docs])

    final_prompt = f"""
{user_prompt}

Context:
{context}

Customer Issue:
{query}
"""

    # Step 4: Call LLM
    response_text, usage = call_llm(final_prompt, temperature, max_tokens)

    # Step 5: Logging
    logger.info(f"QUERY: {query}")
    logger.info(f"PROMPT: {final_prompt}")
    logger.info(f"TEMP: {temperature}, TOKENS: {max_tokens}")
    logger.info(f"USAGE: {usage}")

    return {
        "response": response_text,
        "sources": docs,
        "usage": usage
    }