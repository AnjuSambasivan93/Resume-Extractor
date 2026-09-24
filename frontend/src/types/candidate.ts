export type Candidate = {
    name: string
    email: string
    phone: string
    location: string
    skills: string[]
    education: string[]
    work_experience: string[]
    certifications: string[]
    match_score: number
}

export type CandidateResults ={
    filename: string
    candidate: Candidate
}