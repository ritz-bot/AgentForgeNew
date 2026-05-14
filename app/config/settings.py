from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    # Keep only normal chat-capable models in the UI.
    ALLOWED_MODEL_NAMES = [
        "openai/gpt-oss-120b",
        "llama-3.3-70b-versatile",
        "qwen/qwen3-32b",
    ]

    DEFAULT_SYSTEM_PROMPT = "You are a helpful AI assistant. Answer clearly and accurately."
    AGENT_RECURSION_LIMIT = 8
    BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:9999/chat")
    BACKEND_TIMEOUT_SECONDS = int(os.getenv("BACKEND_TIMEOUT_SECONDS", "90"))


settings = Settings()
