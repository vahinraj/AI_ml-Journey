def normalize_skill(skill):
    skill = skill.lower().strip()

    synonyms = {
        "ml": "machine learning",
        "machine learning": "machine learning",
        "nlp": "natural language processing",
        "natural language processing": "natural language processing",
        "natural processing language": "natural language processing",
        "ai": "artificial intelligence",
        "dl": "deep learning",
        "deep learning": "deep learning"
    }

    return synonyms.get(skill, skill)



def match_skills(resume_skills, job_skills):
    normalized_resume = [normalize_skill(s) for s in resume_skills]
    normalized_job = [normalize_skill(s) for s in job_skills]

    resume_set = set(normalized_resume)
    job_set = set(normalized_job)

    matched = resume_set.intersection(job_set)
    missing = job_set.difference(resume_set)

    score = 0
    for job_skill in job_set:
        if job_skill in resume_set:
            score += 1
        else:
            for res_skill in resume_set:
                if job_skill in res_skill or res_skill in job_skill:
                    score += 0.5
                    break

    if len(job_set) == 0:
        match_percentage = 0
    else:
        match_percentage = (score / len(job_set)) * 100

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }
