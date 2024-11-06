import google.generativeai as genai
from app.core.config import settings

def generate_idea(prompt: str) -> str:
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()
