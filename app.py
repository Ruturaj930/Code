from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import time
from typing import Dict

# Simple Governor: rate limit per client IP (placeholder)
_RATE_LIMIT = 5  # max requests per minute
_last_requests: Dict[str, float] = {}

app = FastAPI(title="Arvi Life Coach Agent")

class RequestBody(BaseModel):
    text: str

def rate_limited():
    client_ip = "127.0.0.1"  # placeholder; use request.client.host in real deployment
    now = time.time()
    if client_ip not in _last_requests:
        _last_requests[client_ip] = now
        return True
    if now - _last_requests[client_ip] < 60 / _RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests, please wait.")
    _last_requests[client_ip] = now
    return True

def get_advice(text: str) -> str:
    # Placeholder for LangChain pipeline
    return f"Based on your question about '{text}', here's some life coaching advice: take a deep breath, stay focused, and remember that every step forward counts."

@app.post("/advice")
@rate_limited()
async def get_life_advice(body: RequestBody):
    advice = get_advice(body.text)
    return {"advice": advice}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)