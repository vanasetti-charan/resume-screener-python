📄 Smart Resume Screening & Shortlisting System (Python)

🚀 A Python-based tool to automate resume screening and candidate shortlisting using skill-based matching.

This project is a Python-based Resume Screening System that automates the process of evaluating and shortlisting candidates based on job-specific skills.

It reads resumes in PDF and DOCX formats, extracts relevant information, and compares it with predefined job requirements to generate a score and shortlist decision.

🎯 Key Features
📂 Processes multiple resumes from a folder
📄 Supports PDF & DOCX formats
🔍 Skill-based matching for different job roles
📊 Resume scoring system (%)
✅ Automatic shortlisting based on threshold
📈 Sorts candidates based on score
📁 Exports results to Excel (result.xlsx)

🛠️ Tech Stack
Python
Pandas
PyPDF2
python-docx
OS module

📂 Project Structure
resume-screener-python/
├── sample.py
├── skill_matching.py
└── Resumes-folder/
    ├── ATS_Friendly_IT_Fresher_Resume_Mahendra.docx
    ├── Charan Python Resume.docx
    ├── Charan-Resume.pdf
    ├── Manasa resume.pdf
    ├── My Resume.docx
    └── Sr.Quality Engineer Resume (1).pdf
├── README.md

📊 Sample Results (Real Test Data)

The system was tested on multiple resumes:
| Resume Name                             | Score (%) | Status         |
| --------------------------------------- | --------- | -------------  |
| ATS_Friendly_IT_Fresher_Resume_Mahendra | 80%+      | ✅ Shortlisted |
| Charan Python Resume                    | 85%+      | ✅ Shortlisted |
| Charan-Resume                           | 70%+      | ✅ Shortlisted |
| Manasa Resume                           | 60–70%    | ⚠️ Borderline  |
| My Resume                               | 65%       | ✅ Shortlisted |
| Sr. Quality Engineer Resume             | 20–40%    | ❌ Rejected    |

📸 Output Screenshots
<img width="1041" height="202" alt="image" src="https://github.com/user-attachments/assets/08e2ee83-f5d7-4f0a-b095-eb0a6447c336" />

📌 How It Works
User enters a job role (e.g., python developer)
System loads required skills for that role
Reads all resumes from the Resumes-folder
Extracts text from each file
Matches skills using keyword-based logic
Calculates:
Matched skills
Resume score (%)
Shortlist status
Generates:
Console output
Excel file (result.xlsx)
🧠 Skill Matching Logic
Each job role has predefined skills
Matching is done using keyword search
Shortlisting condition:

👉 Candidate must match at least 60% of required skills

▶️ How to Run

1. Clone the repository
git clone https://github.com/vanasetti-charan/resume-screener-python.git
cd resume-screener-python

2. Install dependencies
pip install pandas PyPDF2 python-docx

3. Update folder path (if needed)
address = r"E:\Charan\Resumes-folder"

4. Run the program
python sample.py

5. Enter job title
python developer

📊 Output
🖥️ Console Output
Resume name
Matched skills
Resume score
Shortlisted / Rejected
📁 Excel Output
All resumes sorted by score
File: result.xlsx


💡 Why This Project?

Recruiters often receive hundreds of resumes for a single job role, making manual screening time-consuming and inefficient.

This project automates the initial screening process by analyzing resumes based on required skills, helping identify the most relevant candidates quickly and efficiently.

This tool helps:

Automate resume filtering
Save time
Identify relevant candidates quickly

⚠️ Limitations
Keyword-based matching (no NLP)
Cannot detect synonyms or context
Job roles are predefined
Folder path is hardcoded
🚀 Future Improvements
🔥 Add NLP-based matching (spaCy)
🌐 Build Flask web app
📊 Improve Excel formatting
🔎 Add fuzzy matching
☁️ Deploy online
👨‍💻 Author

Vanasetti Charan
Aspiring Python Backend Developer 🚀

⭐ Support

If you like this project:

⭐ Star the repo
🔗 Share on LinkedIn
