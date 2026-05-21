import os
import time
from google import genai

# Don't use load_dotenv on production — Render injects env vars directly
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

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

    print(f"Gemini API Key loaded: {'YES' if os.getenv('GEMINI_API_KEY') else 'NO'}")

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"Gemini error: {e}")
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"Gemini unavailable, retrying in 30s... (attempt {attempt+1}/3)")
                time.sleep(30)
            else:
                raise e

    return "Summary unavailable — Gemini API is temporarily overloaded. Please try again."