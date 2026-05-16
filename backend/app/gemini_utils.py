import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_meeting_summary(transcript):

    prompt = f"""
    You are an AI meeting assistant.

    Analyze the following meeting transcript and generate:

    1. Meeting Summary
    2. Key Discussion Points
    3. Action Items
    4. Final Decisions

    Transcript:
    {transcript}
    """

    # Retry up to 3 times on server errors
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"Gemini unavailable, retrying in 30s... (attempt {attempt+1}/3)")
                time.sleep(30)
            else:
                raise e

    return "Summary unavailable — Gemini API is temporarily overloaded. Please try again."