import json
from pathlib import Path

from pdf_reader import extract_text_from_pdf
from resume_extractor import extract_candidate_data
resume_folder = Path("./sample_resumes")

all_candidates = []

for pdf_file in resume_folder.glob("*.pdf"):
    print(f"Processing resume: {pdf_file.name}")
    resume_text = extract_text_from_pdf(pdf_file)
    candidate_info = extract_candidate_data(resume_text)
    candidate_data = json.loads(candidate_info)
    all_candidates.append(candidate_data)

print(all_candidates)
