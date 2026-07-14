import sys
import fitz
from src.state import InterviewState
from src.prompts.resume_prompt import RESUME_ANALYSIS_PROMPT
from src.llm import llm
from src.logger import logging
from src.exceptions import CustomException

structured_llm = llm.with_structured_output(ResumeAnalysis)


def extract_resume_text(pdf_path: str) -> str:
    logging.info(f"Reading resume from: {pdf_path}")
    document = fitz.open(pdf_path)
    resume_text = ""
    for page in document:
        resume_text += page.get_text()
    document.close()

    return resume_text.strip()

def resume_agent(state:InterviewState):
    try:
        logging.info("Resume Agent Started")

        pdf_path = state["resume_path"]
        resume_text = extract_resume_text(pdf_path)
        prompt = RESUME_ANALYSIS_PROMPT.format(resume=resume_text)
        result = structured_llm.invoke(prompt)     
        return {
           "skills":response.skills,
           "projects":response.projects,
           "technologies":response.technologies,
           "candidate_role":response.candidate_role,
           "experience_level":response.experience_level
        }
    except Exception as e:
        raise CustomException(e,sys)



