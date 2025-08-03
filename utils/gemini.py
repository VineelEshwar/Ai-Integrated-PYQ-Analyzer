import os
from dotenv import load_dotenv
import google.generativeai as genai

def init_gemini(model_name: str = "gemini-1.5-flash"):
    """
    Initializes Gemini model using API key from environment variable.
    
    Args:
        model_name (str): The Gemini model to load.
                         Options: "gemini-1.5-flash", "gemini-1.5-pro" etc.

    Returns:
        genai.GenerativeModel: Initialized Gemini model instance.

    Raises:
        ValueError: If API key is missing or model fails to load.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY not found in .env or environment variables.")

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        return model
    except Exception as e:
        raise RuntimeError(f"❌ Failed to initialize Gemini model: {e}")
