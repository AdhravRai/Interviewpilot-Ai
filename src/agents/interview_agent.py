import sys
from src.state import InterviewState
from src.models import InterviewQuestion
from src.logger import logging
from src.exceptions import CustomException


def interview_agent(state: InterviewState):
    try:
        questions =state["questions"]
        question_index=state["question_index"]
        logging.info("Interview Agent Started")
        if question_index >= len(questions):
            logging.info("Interview completed")
            return 
        current_question=questions[question_index]
        logging.info(f"Serving question {question_index + 1}")
        return {
            "current_question":current_question
        }
    except Exception as e:
        raise CustomException(e, sys)