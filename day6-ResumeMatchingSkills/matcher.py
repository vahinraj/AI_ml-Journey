def match_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set.difference(resume_set)

    if(len(job_set) == 0):
        match_percentage = 0
    else:
        match_percentage = (len(matched_skills) / len(job_set)) * 100
    
    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }