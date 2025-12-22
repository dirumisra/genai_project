# grokai_client_setup.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env.dev
load_dotenv("C:/Users/dhira/Desktop/genai_project/envs/.env.dev")

# Read the Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# If the API key is missing, raise an error
if not groq_api_key:
    raise RuntimeError("❌ GROQ_API_KEY is missing. Please check your .env file.")

# Initialize the Groq client (OpenAI-compatible)
client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

print("✅ Groq client configured successfully and ready to use.")
