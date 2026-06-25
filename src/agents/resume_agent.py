import sys
from src.state import InterviewState
from src.prompts.resume_prompt import RESUME_ANALYSIS_PROMPT
from src.llm import llm

def resume_agent(state:InterviewState):
    try:
     resume_text=state["resume_text"]
     prompt = f" Prompt : {RESUME_ANALYSIS_PROMPT}  Resume : {resume_text} "
     resume_llm =llm.with_structured_output(ResumeAnalysis)
     response=resume_llm.invoke(prompt)
     print(type(response))
     return {
        "skills":response.skills,
        "projects":response.projects,
        "technologies":response.technologies,
        "candidate_role":response.candidate_role,
        "experience_level":response.experience_level
     }
    except Exception as e:
        raise CustomException(e,sys)



