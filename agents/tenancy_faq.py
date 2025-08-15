# agents/tenancy_faq.py

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")

def answer_tenancy_question(user_question, location=None):
    prompt = (
        "You are a helpful legal assistant specializing in tenancy laws, rent agreements, "
        "landlord-tenant rights, and rental procedures."
    )

    if location:
        prompt += f" The user is from {location}, so provide region-specific advice if relevant."

    prompt += f"\n\nUser Question: {user_question}\n\nAnswer:"

    response = model.generate_content(prompt)
    return response.text.strip()
