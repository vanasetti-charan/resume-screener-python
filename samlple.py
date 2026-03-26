from PyPDF2 import PdfReader
from docx import Document
import os
from skill_matching import skill_match
import pandas as pd
#reading Resumes in format of PDF
class ReadingResumes:
    @staticmethod
    def read_pdf(resume):
        with open(resume,'rb') as f:
            pdf =PdfReader(f)
            text = []
            pages = pdf.pages
            for page in pages:
                text.append(page.extract_text() or "")
        return " ".join(text).lower()
    #reading Resumes in format of DOC
    @staticmethod
    def read_doc(resume):
        doc = Document(resume)
        text = [para.text for para in doc.paragraphs]
        return " ".join(text).lower()

class Shortlisting(ReadingResumes):
    def __init__(self,resume_file,job_title):
        self.result = None
        try :
            if not os.path.exists(resume_file):
                print(f"No such file exists :{resume_file}")
                return
            elif resume_file.lower().endswith(".pdf"):
                text = self.read_pdf(resume_file)
            elif resume_file.lower().endswith(".docx"):
                text = self.read_doc(resume_file)
            else:
                print(f"Resume format not supported : {resume_file}")
                return
            matched,score,shortlisted = skill_match(text,job_title)
            self.result = {
                "resume":resume_file,
                "matched":matched,
                "score":score,
                "shortlisted":shortlisted
            }
        except Exception as e :
            print(f": {e}")

class ReadingFolder:
    def __init__(self):
        address = r"E:\Charan\Resumes-folder"
        job_title = input("Please enter the job title : ").lower()

        if not os.path.exists(address):
            print(f"No such directory exists :{address}")
            return
        resumes = [file for file in os.listdir(address) if file.lower().endswith((".pdf",".docx"))]
        if not resumes:
            print(f"No PDF/DOCX file is exist in this directory :{address}")
        else:
            result = []
            for resume in resumes:
                resume = os.path.join(address, resume)
                obj = Shortlisting(resume,job_title)
                if obj.result:
                    result.append(obj.result)
            result.sort(key=lambda x : x["score"],reverse=True)
            df = pd.DataFrame(result)
            df.to_excel("result.xlsx",index=False)



if __name__ == "__main__":
    ReadingFolder()