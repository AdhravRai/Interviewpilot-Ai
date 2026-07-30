from langgraph.types import interrupt
from src.logger import logging
from src.state import InterviewState
def interview_agent(state: InterviewState):
    questions = state["questions"]
    question_index = state["question_index"]
    logging.info(f"Interview Agent Started : Question {question_index + 1}")
    if question_index >= len(questions):
        logging.info("Interview completed")
        return {}
    current_question = questions[question_index]
    response = interrupt(
        {
            "question": current_question.question,
            "topic": current_question.topic,
            "difficulty": current_question.difficulty,
            "actions": [
                "submit",
                "stop",
            ],
        }
    )

    if response.get("action") == "stop":
        logging.info("Interview stopped by user.")
        return {
            "stop_requested": True,
        }
    return {
        "current_question": current_question,
        "current_answer": response.get("answer", ""),
    }