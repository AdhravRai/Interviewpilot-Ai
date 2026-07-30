import sys
from src.llm import llm
from src.logger import logging
from src.exceptions import CustomException
from src.prompts.difficulty_adaptation_prompt import DIFFICULTY_ADAPTATION_PROMPT
from src.models import DifficultyAdaptationResult
from src.state import InterviewState

structured_llm=llm.with_structured_output(DifficultyAdaptationResult)

def difficulty_adaptation_agent(state:InterviewState):
    try:
        logging.info("Difficulty Adaptation Agent Started")
        if state["stop_requested"]:
            logging.info("Interview stopped. Skipping difficulty adaptation.")
            return {}
        difficulty_level=state["difficulty_level"]
        history=state["interview_history"]

        prompt=f"""
        Instructions :
        {DIFFICULTY_ADAPTATION_PROMPT}

        Evaluation Context:
        {history}

        Difficulty Level:
        {difficulty_level}

        """        
        result=structured_llm.invoke(prompt)
        logging.info(f"Difficulty changed from {difficulty_level} to {result.difficulty_level}" )
        return{
            "difficulty_level" : result.difficulty_level
        }

    except Exception as e:
        raise CustomException(e,sys)