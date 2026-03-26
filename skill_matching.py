
skills = { "python developer" : ["python","data structures","rest apis","django","sql","git"],
               "backend developer": ["python", "java", "node.js", "rest apis", "databases", "system design", "git"],
                "data analyst": ["python", "pandas", "numpy", "sql", "excel", "data visualization"],
                "data scientist": ["python", "machine learning", "statistics", "pandas", "scikit-learn", "data visualization"],
                "full stack developer": ["html", "css", "javascript", "react", "node.js", "sql", "git"],
                "frontend developer": ["html", "css", "javascript", "react", "bootstrap", "git"],
                "devops engineer": ["linux", "docker", "kubernetes", "ci/cd", "aws", "python"],
                "software engineer": ["programming", "data structures", "algorithms", "system design", "git", "databases"],
                "machine learning engineer": ["python", "machine learning", "tensorflow", "pandas", "numpy", "sql"],
                "automation engineer": ["python", "selenium", "automation testing", "pytest", "git"]
    }
def skill_match(file_text,job_title):
    job_skill = skills.get(job_title,[])
    matched = [skill for skill in job_skill if skill.lower() in file_text]
    threshold = int(len(job_skill) *0.6)
    resume_score = (len(matched) / len(job_skill)) * 100 if job_skill else 0
    shortlisted = len(matched) >= threshold
    return matched, int(resume_score), shortlisted





