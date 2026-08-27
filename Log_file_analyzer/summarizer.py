from dotenv import load_dotenv
import os
from google import genai
import time

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize(stats: dict, retries: int = 3) -> str:
    prompt = f""" You are a log file analyzer. You have been given the following statistics from a log file analyze the given logs and give 2-3 lines summary {stats}"""
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            if attempt == retries - 1:
                raise
            print(f"Retry {attempt + 1}/{retries} after error: {e}")
            time.sleep(2)