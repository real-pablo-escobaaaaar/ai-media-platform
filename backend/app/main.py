from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="AI Media Generation Platform API")

class MediaRequest(BaseModel):
    prompt: str
    model_name: str
    aspect_ratio: str = "16:9"

@app.get("/")
def read_root():
    return {"status": "online", "message": "AI Engine is running"}

@app.post("/generate")
async def generate_media(request: MediaRequest):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API Key not configured")

    return {
        "status": "processing",
        "prompt": request.prompt,
        "selected_model": request.model_name,
        "message": "Task queued successfully"
    }
