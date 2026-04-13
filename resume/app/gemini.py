import os
# from google import genai
import google.generativeai as genai
import json

client = genai.Client()

def analyze_resume(resume_text, job_desc):
    prompt = f"""
    Compare the resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}

    Return clearly:
    1. Matching skills
    2. Missing skills
    3. Score out of 100
    4. Learning roadmap
    """

    # Call generate_content directly from the client, passing the model name
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text