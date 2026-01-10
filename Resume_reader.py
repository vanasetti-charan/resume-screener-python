from PyPDF2 import PdfReader
from docx import Document
import os

# --- Job Description Skills ---
job_skills = ["python", "java", "c", "power-bi", "sql", "machine learning", "c++"]

# -------- PDF Reader --------
def read_pdf(resume_file):
    """Extract text from PDF file"""
    try:
        with open(resume_file, "rb") as f:
            reader = PdfReader(f)
            text = [page.extract_text() for page in reader.pages if page.extract_text()]
        return " ".join(text).lower()
    except Exception as e:
        print(f"Error reading PDF {resume_file}: {e}")
        return ""

# -------- DOCX Reader --------
def read_docx(resume_file):
    """Extract text from DOCX file"""
    try:
        doc = Document(resume_file)
        text = [para.text for para in doc.paragraphs]
        return " ".join(text).lower()
    except Exception as e:
        print(f"Error reading DOCX {resume_file}: {e}")
        return ""

# -------- Skill Matching --------
def match_skills(file_text, job_skills):
    """Match resume text with job skills"""
    matched = [skill for skill in job_skills if skill.lower() in file_text]
    threshold = len(job_skills) // 2  # at least half skills required to shortlist
    resume_score = (len(matched) / len(job_skills)) * 100
    shortlisted = len(matched) >= threshold
    return matched, resume_score, shortlisted

# -------- File Matching --------
def file_match(resume_file, job_skills):
    """Process a single resume file"""
    if not os.path.exists(resume_file):
        print(f"File doesn't exist: {resume_file}")
        return

    ext = resume_file.lower()
    if ext.endswith(".pdf"):
        text = read_pdf(resume_file)
    elif ext.endswith(".docx"):
        text = read_docx(resume_file)
    else:
        print(f"Unsupported file format: {resume_file}")
        return

    matched, score, shortlisted = match_skills(text, job_skills)

    # Print result
    print("\n" + "*" * 40)
    print(f"Resume: {resume_file}")
    if shortlisted:
        print("Shortlisted!")
    else:
        print("Rejected")
    print(f"Matched skills: {matched}")
    print(f"Resume score: {score:.2f}%")
    print("*" * 40 + "\n")

# -------- Run Program --------
    # Single sample resume in same folder as script
    resume_file = "Charan-Resume.pdf"  
    file_match(resume_file, job_skills)
