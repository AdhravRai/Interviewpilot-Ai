import sys
from src.llm import llm
from src.models import FeedbackResult
from src.logger import logging
from src.exceptions import CustomException
from src.state import InterviewState
from src.prompts.feedback_prompt import FEEDBACK_PROMPT


structured_llm=llm.with_structured_output(FeedbackResult)

def feedback_agent(state:InterviewState):
    try:
        logging.info("Feedback Agent Started")
        evaluations = state["evaluations"]
        interview_history=state["interview_history"]
        interview_plan=state["interview_plan"]

        prompt=f"""
        Instructions :
        {FEEDBACK_PROMPT}

        Evaluations:
        {evaluations}

        Interview Context History :
        {interview_history}

        Interview Plan:
        {interview_plan}

        """
        result=structured_llm.invoke(prompt)
        logging.info("Feedback generated successfully")

        return {
            "feedback" : result
        }
    except Exception as e:
        raise CustomException(e,sys)