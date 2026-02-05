import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    tokens = word_tokenize(resume_text)

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalpha() and word not in stop_words
    ]
    skills_db = [
        "python", "java", "c++", "machine learning", "data analysis",
        "project management", "communication", "teamwork", "sql",
        "javascript", "html", "css", "react", "node.js", "aws",
        "docker", "kubernetes", "git", "linux", "agile"
    ]
    found_skills = set()
    for skill in skills_db:
        skill_tokens = skill.split()
        if all(token in filtered_tokens for token in skill_tokens):
            found_skills.add(skill)
    return list(found_skills)
