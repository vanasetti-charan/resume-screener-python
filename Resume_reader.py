from PyPDF2 import PdfReader
from docx import Document
import os

# --- Job Description Skills ---
job_skills = ["python", "java", "c", "power-bi", "sql", "machine learning", "c++"]

# -------- PDF Reader --------
def read_pdf(resume_file):
    try:
        with open(resume_file, "rb") as f:
            reader = PdfReader(f)
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return " ".join(text).lower()  # join with spaces to preserve words
    except Exception as e:
        print(f"Error reading PDF {resume_file}: {e}")
        return ""

# -------- DOCX Reader --------
def read_docx(resume_file):
    try:
        doc = Document(resume_file)
        text = [para.text for para in doc.paragraphs]
        return " ".join(text).lower()  # join with spaces
    except Exception as e:
        print(f"Error reading DOCX {resume_file}: {e}")
        return ""

# -------- Skill Matching --------
def match_skills(file_text, job_skills):
    matched = [skill for skill in job_skills if skill.lower() in file_text]
    threshold = len(job_skills) // 2
    resume_score = (len(matched) / len(job_skills)) * 100
    shortlisted = len(matched) >= threshold
    return matched, resume_score, shortlisted

# -------- File Matching --------
def file_match(resume_file, job_skills):
    if not os.path.exists(resume_file):
        print(f"File doesn't exist: {resume_file}")
        return

    # Case-insensitive extension check
    if resume_file.lower().endswith(".pdf"):
        text = read_pdf(resume_file)
    elif resume_file.lower().endswith(".docx"):
        text = read_docx(resume_file)
    else:
        print(f"Unsupported file format: {resume_file}")
        return

    matched, score, shortlisted = match_skills(text, job_skills)
    
    # Print result
    print(f"\nResume: {resume_file}")
    if shortlisted:
        print("Shortlisted!")
    else:
        print("Rejected")
    print(f"Matched skills: {matched}")
    print(f"Resume score: {score:.2f}%")

# -------- Process All Resumes in Folder --------
def read_folder(job_skills, folder_path="Resumes-folder"):
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return

    files = os.listdir(folder_path)
    resumes = [file for file in files if file.lower().endswith((".pdf", ".docx"))]

    if not resumes:
        print("No PDF or DOCX resumes found in this folder")
        return

    print(f"Found {len(resumes)} resumes. Processing...\n")

    for resume in resumes:
        resume_file = os.path.join(folder_path, resume)
        print(f"Processing: {resume}")
        file_match(resume_file, job_skills)

# ---------Set your folder path here---------

folder_path = "Resumes-folder"

# -------- Run Program --------

read_folder(job_skills, folder_path)
