# agents/issue_detector.py

import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")  # or "gemini-1.5-flash"

def detect_issues(image_path, user_text=None):
    image = Image.open(image_path)

    parts = [
        {
            "text": (
                "You're a real estate expert. Analyze the image and describe any visible property issues "
                "(like mold, water damage, cracks, poor lighting, broken fixtures). "
                "Suggest possible causes and what action the user should take."
            )
        },
        image  # PIL image directly
    ]

    if user_text:
        parts.insert(1, {"text": f"User says: {user_text}"})

    response = model.generate_content(parts)
    return response.text
