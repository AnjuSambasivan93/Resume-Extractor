import json
from pathlib import Path

from pdf_reader import extract_text_from_pdf
from resume_extractor import extract_candidate_data
from database import save_candidate
from models import Candidate
from matcher import calculate_match_score, find_skill_matches

resume_folder = Path("./sample_resumes")

all_candidates = []

for pdf_file in resume_folder.glob("*.pdf"):
    print(f"Processing resume: {pdf_file.name}")
    resume_text = extract_text_from_pdf(pdf_file)
    candidate_info = extract_candidate_data(resume_text)
    candidate_data = json.loads(candidate_info)
    candidate = Candidate(**candidate_data)
    save_candidate(candidate.model_dump())
    all_candidates.append(candidate_data)

print(all_candidates)

job_description = """We are looking for a Data Analyst with Python, SQL, Power BI,
Excel and data analysis experience."""

for candidate in all_candidates:
    score = calculate_match_score(job_description, candidate)
    matched_skills, missing_skills = find_skill_matches(job_description, candidate)
    candidate["match_score"] = score
    candidate["matched_skills"] = matched_skills
    candidate["missing_skills"] = missing_skills

ranked_candidates = sorted(all_candidates, key=lambda candidate: candidate["match_score"], reverse=True)

for candidate in ranked_candidates:
    print(candidate['name'], candidate['match_score'])
    print("Matched Skills:", candidate['matched_skills'])
    print("Missing Skills:", candidate['missing_skills'])
    print("--------------------------------------------------")