import os
from dotenv import load_dotenv

load_dotenv()  

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    PROJECT_NAME: str = "WebChat IA"
    API_V1_STR: str = "/api/v1"

settings = Settings()
