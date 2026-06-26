import sys
from src.llm import llm
from src.prompts.skillgap_prompt import SKILL_GAP_PROMPT
from src.logger import logging
from src.exceptions import CustomException
from src.models import SkillGapResult

def skill_gap_agent(state:InterviewState):
    try:
        candidate_profile={
            "skills":state["skills"],
            "projects":state["projects"],
            "technologies":state["technologies"],
            "candidate_role":state["candidate_role"]            
        }
        prompt =f" Instructions :{SKILL_GAP_PROMPT}  Candidate profiel :{candidate_profile}"
        logging.info("Starting Skill Gap Analysis")
        skill_gap_llm=llm.with_structured_output(SkillGapResult)
        response =skill_gap_llm.invoke(prompt)
        
        logging.info("Skill Gap Analysis completed successfully")
        return {
            "weak_areas":response.weak_areas
        }
    except Exception as e:
        raise CustomException(e,sys)