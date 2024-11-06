from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import generate_idea
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)

class IdeaRequest(BaseModel):
    prompt: str

@router.post("/generate-idea")
async def get_idea(request: IdeaRequest):
    try:
        idea = generate_idea(request.prompt)
        return {"idea": idea}
    except Exception as e:
        logging.error(f"Error generating idea: {e}")
        raise HTTPException(status_code=500, detail="Error generating idea.")
