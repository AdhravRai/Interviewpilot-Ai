import sys
from src.prompts.interview_plan_prompt import INTERVIEW_PLANNER_PROMPT
from src.models import InterviewPlanner
from src.logger import logging
from src.exceptions import CustomException
from src.llm import llm
from src.state import InterviewState

def interview_plan_agent(state:InterviewState):
    try:
        candidate_profile={
            "skills":state["skills"],
            "projects":state["projects"],
            "technologies":state["technologies"],
            "candidate_role":state["candidate_role"],
            "experience":state["experience_level"],
            "weak_areas":state["weak_areas"]               
        }
        prompt=f"""
        Instruction for the plan : 
        {INTERVIEW_PLANNER_PROMPT}

        Candidate's profile :
        {candidate_profile}"""
        interview_plan_llm=llm.with_structured_output(InterviewPlanner)
        logging.info("Interview Planner Agent :Generating plan for the interview")
        result=interview_plan_llm.invoke(prompt)
        plan = result.interview_topics
        difficulty = result.starting_difficulty  
        return {
            "interview_plan":plan,
            "difficulty_level":difficulty
        }
    except Exception as e:
        raise CustomException(e,sys)

