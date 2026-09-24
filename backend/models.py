from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    email: str
    phone: str
    location: str
    skills: list[str]
    education: list[str]
    work_experience: list[str]
    certifications: list[str]