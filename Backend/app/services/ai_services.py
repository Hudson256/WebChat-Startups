import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_idea(prompt: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
