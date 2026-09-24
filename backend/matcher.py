from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(job_description, candidate):
    candidate_text = " ".join(candidate["skills"]
                              + candidate["education"]
                              + candidate["work_experience"]
                              + candidate["certifications"]
    )
    texts = [job_description, candidate_text]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    job_vector = vectors[0]
    candidate_vector = vectors[1]

    score = cosine_similarity(job_vector, candidate_vector).item()

    return round(score * 100, 2)

def find_skill_matches(job_description, candidate):
    job_text = job_description.lower()
    matched_skills = []
    missing_skills = []

    for skill in candidate["skills"]:
        if skill.lower() in job_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills
