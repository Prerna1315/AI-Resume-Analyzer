import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)


def analyze_resume(text):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Analyze this resume.

Give:

1. Resume Summary

2. Strengths

3. Weaknesses

4. ATS Score out of 100

5. Suggestions for improvement


Resume:

{text}
"""

    response = model.generate_content(prompt)

    return response.text