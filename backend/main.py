import pymupdf
from fastapi import FastAPI, UploadFile, File, Form
from resume_extractor import extract_candidate_data
import json
from models import Candidate
from database import save_candidate, create_table
from matcher import calculate_match_score, find_skill_matches

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
create_table()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Resume Builder API is running!"}

@app.post("/upload-resume/")
async def upload_resume(files: list[UploadFile] = File(...)):
   results = []
   for file in files:
      contents = await file.read()

   document = pymupdf.open(stream=contents, filetype="pdf")
   text = ""
   for page in document:
       text += page.get_text()
   document.close()

   candidate_info = extract_candidate_data(text)
   candidate_data = json.loads(candidate_info)
   candidate = Candidate(**candidate_data)
   save_candidate(candidate.model_dump())
   results.append({"filename": file.filename, "candidate": candidate.model_dump()})


   return results

@app.post("/analyze/")
async def analyze_resume(job_description: str = Form(...), files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        contents = await file.read()

        document = pymupdf.open(stream=contents, filetype="pdf")
        text = ""
        for page in document:
            text += page.get_text()
        document.close()

        candidate_info = extract_candidate_data(text)
        candidate_data = json.loads(candidate_info)
        candidate = Candidate(**candidate_data)
        candidate_dict = candidate.model_dump()
        score = calculate_match_score(job_description, candidate_dict)
        candidate_dict["match_score"] = score
        save_candidate(candidate.model_dump())

        score = calculate_match_score(job_description, candidate_data)
        matched_skills, missing_skills = find_skill_matches(job_description, candidate_data)

        results.append({
            "filename": file.filename,
            "candidate": candidate_dict,
        })
        results = sorted(results, key=lambda result: result["candidate"]["match_score"], reverse=True)


    return results