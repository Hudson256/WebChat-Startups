import google.generativeai as genai
from app.core.config import settings

def generate_idea(prompt: str) -> str:
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    formatted_response = format_response(response.text)
    return formatted_response

def format_response(response_text: str) -> str:
    formatted_text = response_text.replace("**", "")
    formatted_text = formatted_text.replace(": ", ":")
    formatted_text = formatted_text.replace("\n", "<br/>")
    formatted_text = formatted_text.replace("* ", "<br/><br/>* ")
    formatted_text = formatted_text.replace("  ", " ")
    return formatted_text.strip()
