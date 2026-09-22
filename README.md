# AI Resume Extractor & Candidate Matcher

A full-stack AI-powered application that extracts structured information from PDF resumes, compares multiple candidates against a job description, and ranks candidates based on their match score.

## Overview

Reviewing multiple resumes manually can be time-consuming, especially when resumes have different formats and layouts.

This application provides a structured workflow for resume screening. Users can enter a job description and upload multiple PDF resumes. The system extracts candidate information using an LLM, validates the extracted data, calculates candidate-job similarity, and returns ranked candidates through a React interface.

## Features

- Upload multiple PDF resumes
- Enter a job description
- Extract resume text using PyMuPDF
- Extract structured candidate information using an LLM
- Validate AI-generated data using Pydantic
- Store candidate information in SQLite
- Compare candidates with the job description using TF-IDF
- Calculate match scores using cosine similarity
- Rank candidates by match score
- Display candidate results through a React frontend

## Extracted Information

The application extracts:

- Name
- Email
- Phone
- Location
- Skills
- Education
- Work experience
- Certifications

Different resume formats are converted into a consistent structured format before further processing.

## Application Workflow

```text
Job Description + PDF Resumes
              ↓
        React Frontend
              ↓
        FastAPI Backend
              ↓
      PDF Text Extraction
              ↓
       LLM Extraction
              ↓
     Pydantic Validation
              ↓
       SQLite Storage
              ↓
    TF-IDF Vectorization
              ↓
     Cosine Similarity
              ↓
       Match Scores
              ↓
    Candidate Ranking
              ↓
      Results Display
```

## Technology Stack

**Frontend**
- React
- TypeScript
- Vite
- Zustand
- CSS

**Backend**
- Python
- FastAPI
- Pydantic
- PyMuPDF

**AI**
- Hugging Face Inference API
- Structured LLM output

**Matching**
- Scikit-learn
- TF-IDF
- Cosine Similarity

**Database**
- SQLite

## Project Structure

```text
RESUME_EXTRACTOR/
├── backend/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── resume_extractor.py
│   ├── models.py
│   ├── matcher.py
│   └── database.py
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── services/
│       ├── store/
│       ├── types/
│       ├── App.tsx
│       ├── main.tsx
│       └── styles.css
│
├── sample_resumes/
├── .gitignore
└── README.md
```

## Candidate Matching

Candidate information and the job description are converted into numerical vectors using TF-IDF.

Cosine similarity is then used to calculate the similarity between the job description and each candidate profile.

Candidates are ranked from the highest match score to the lowest.

## Running the Application

### Backend

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

FastAPI runs at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Frontend

Move to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend runs at:

```text
http://localhost:5173
```

## Environment Variables

The Hugging Face API token is stored in an environment file and is not committed to the repository.

```text
HF_TOKEN=hugging_face_token
```

## Current Status

The core backend pipeline for PDF extraction, AI-based structured data extraction, validation, database storage, candidate matching, and ranking has been implemented.

The React and TypeScript frontend is currently being developed to display and manage candidate analysis results.

## Planned Improvements

- Improved candidate result interface
- Loading and error handling
- Matched and missing skill analysis
- CSV export
- Semantic matching using embeddings
- Analysis history
- Docker containerization
- Automated testing and CI/CD
