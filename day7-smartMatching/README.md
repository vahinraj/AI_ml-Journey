# Day 7 – Smart Resume ↔ Job Matching (Semantic Matching)

This module upgrades the Resume Analyzer from basic keyword matching to
semantic and intelligent skill matching, similar to real ATS systems.

------------------------------------------------------------

FEATURES
- Extracts skills from resume and job description
- Normalizes skills using synonyms (ML → Machine Learning, NLP → Natural Language Processing)
- Supports partial and semantic matching
- Calculates realistic match percentage
- Shows matched and missing skills

------------------------------------------------------------

HOW IT WORKS

1. Resume and job description text are read
2. Skills are extracted using NLP
3. Skills are normalized using a synonym dictionary
4. Matching is done using:
   - Exact match → full score
   - Partial match → half score
5. Final match percentage is calculated

------------------------------------------------------------

PROJECT STRUCTURE

day7-smart-matching/
│
├── main.py
├── resume_reader.py
├── skill_extractor.py
├── matcher.py
├── sample_resume.txt
├── job_description.txt
├── requirements.txt
└── README.md

------------------------------------------------------------

HOW TO RUN

Open terminal inside this folder and run:

python main.py

------------------------------------------------------------

EXAMPLE OUTPUT

Match Percentage: 80%
Matched Skills: python, machine learning, sql, git
Missing Skills: deep learning

------------------------------------------------------------

TECH STACK

Python  
NLTK  
Basic NLP  
Rule-based semantic matching  

------------------------------------------------------------

WHY THIS PROJECT MATTERS

This simulates how real-world ATS (Applicant Tracking Systems)
evaluate resumes against job requirements and improves accuracy
beyond simple keyword matching.

------------------------------------------------------------

NEXT IMPROVEMENTS

- ML similarity scoring (TF-IDF + cosine similarity)
- PDF resume parsing
- Web interface for uploading resumes
