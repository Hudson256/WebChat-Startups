from fastapi import APIRouter, HTTPException
from app.services.ai_service import generate_idea

router = APIRouter()

@router.post("/generate-idea")
async def get_idea(prompt: str):
    try:
        idea = generate_idea(prompt)
        return {"idea": idea}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating idea.")
