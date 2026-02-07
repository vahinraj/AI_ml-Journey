# Day 8 – ML Resume ↔ Job Similarity (TF-IDF + Cosine)

This module adds machine-learning based similarity scoring to the
AI Resume Analyzer. Instead of only matching skills using rules,
we now compare the entire resume and job description using
TF-IDF vectorization and cosine similarity.

------------------------------------------------------------

WHAT THIS DOES

- Reads resume text
- Reads job description text
- Converts both into TF-IDF vectors
- Computes cosine similarity
- Outputs overall match percentage

This simulates how real ATS systems estimate how well a resume
matches a job posting.

------------------------------------------------------------

TECH STACK

Python  
NLTK  
scikit-learn  
TF-IDF  
Cosine Similarity  

------------------------------------------------------------

PROJECT STRUCTURE

day8-ml-similarity/
│
├── main.py
├── resume_reader.py
├── similarity.py
├── sample_resume.txt
├── job_description.txt
├── requirements.txt
└── README.md

------------------------------------------------------------

HOW TO RUN

1. Install dependencies:
pip install -r requirements.txt

2. Run program:
python main.py

------------------------------------------------------------

EXAMPLE OUTPUT

=== ML Similarity Score ===
Overall Resume ↔ Job Match: 76.32%

------------------------------------------------------------

WHY THIS IS IMPORTANT

Traditional resume checkers only look for keywords.
This module compares the full meaning of the resume
and job description using machine learning.

This makes the system closer to real-world ATS tools.

------------------------------------------------------------

NEXT IMPROVEMENTS

- Combine
