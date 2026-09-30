import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)



def extract_candidate_data(resume_text):
    prompt = f"""
        Extract candidate information from this resume.

        Return ONLY valid JSON.

        Use exactly this structure:

        {{
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "skills": [],
        "education": [],
        "work_experience": [],
        "certifications": []
        }}

        Rules:
        - Do not include any extra information or fields.
        - name, email, phone, location must be strings.
        - skills must be a list of strings.
        - education must be a list of strings.
        - work_experience must be a list of strings.
        - certifications must be a list of strings.
        - Do not return dictionaries inside education or work_experience.
        - Do not add extra fields.
        - Do not add explanations.
        - If information is missing, use "" for strings and [] for lists.

        Resume:
        {resume_text}
        """

    response = client.chat_completions.create(
        model="openrouter/free",
        messages = [
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
