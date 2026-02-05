from resume_reader import read_resume
from skill_extractor import extract_skills
from matcher import match_skills

resume_text = read_resume("sample_resume.txt")
job_text = read_resume("job_description.txt")


resume_skills = extract_skills(resume_text)
job_skills = extract_skills(job_text)


result = match_skills(resume_skills, job_skills)

print("\n--- RESULT ---")
print("Match %:", result["match_percentage"])
print("Matched:", result["matched_skills"])
print("Missing:", result["missing_skills"])
