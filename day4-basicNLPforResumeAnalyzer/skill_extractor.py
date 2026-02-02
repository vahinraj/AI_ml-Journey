def extract_skills(resume_text):
    resume_text = resume_text.lower()

    skills_db = ["python", "java", "c++", "machine learning", "data analysis",
                 "project management", "communication", "sql", "aws", "docker", "git"]

    found_skills = []

    for skill in skills_db:
        if skill in resume_text:
            found_skills.append(skill)
    return found_skills