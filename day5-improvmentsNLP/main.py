from resume_reader import read_resume
from skill_extractor import extract_skills

resume_text = read_resume("sample_resume.txt")
skills = extract_skills(resume_text)

print("Extracted Skills:")
for skill in skills:
    print("-", skill)