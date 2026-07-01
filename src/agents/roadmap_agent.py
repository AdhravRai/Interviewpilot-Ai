import sys
from src.llm import llm
from src.models import RoadmapResult
from src.logger import logging
from src.exceptions import CustomException
from src.state import InterviewState
from src.prompts.roadmap_prompt import ROADMAP_PROMPT


structured_llm=llm.with_structured_output(RoadmapResult)

def roadmap_agent(state:InterviewState):
    try:
        logging.info("Roadmap Agent Started")
        feedback=state["feedback"]

        prompt=f"""
        Instructions :
        {ROADMAP_PROMPT}

        Feedback:
        {feedback}

        """
        result=structured_llm.invoke(prompt)
        logging.info("Roadmap generated successfully")

        return {
            "roadmap" : result
        }
    except Exception as e:
        raise CustomException(e,sys)