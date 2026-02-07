from resume_reader import read_resume
from similarity import compute_similarity

resume_text = read_resume("sample_resume.txt")
job_text = read_resume("job_description.txt")

score = compute_similarity(resume_text, job_text)

print("\n=== ML Similarity Score ===")
print(f"Overall Resume ↔ Job Match: {score}%")
