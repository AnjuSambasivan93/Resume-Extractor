import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

client = InferenceClient(provider="auto", token=token)



def extract_candidate_data(resume_text):
    prompt = f"""
    Extract the following information from the resume:
    name
    email
    phone
    location
    skills
    education
    work experience
    certifications

    Returns only valid JSON.

    Resume:
    {resume_text}
    """

    response = client.chat_completion(
        model="Qwen/Qwen3.8-27B",
        messages = [
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message["content"]
