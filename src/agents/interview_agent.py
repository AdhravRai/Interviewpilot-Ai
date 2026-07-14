import sys
from src.state import InterviewState
from src.models import InterviewQuestion
from src.logger import logging
from src.exceptions import CustomException
from langgraph.types import interrupt


def interview_agent(state: InterviewState):
    try:
        questions =state["questions"]
        question_index=state["question_index"]
        logging.info("Interview Agent Started")
        if question_index >= len(questions):
            logging.info("Interview completed")
            return {}
        current_question=questions[question_index]
        logging.info(f"Serving question {question_index + 1}")
        answer = interrupt(
            {
                "question": current_question.question,
                "topic": current_question.topic,
                "difficulty": current_question.difficulty
            }
        )
        return {
            "current_question":current_question,
            "current_answer":answer
        }
    except Exception as e:
        raise CustomException(e, sys)