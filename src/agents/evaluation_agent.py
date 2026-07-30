import sys
from src.logger import logging
from src.exceptions import CustomException
from src.state import InterviewState
from src.prompts.evaluation_prompt import EVALUATION_RESULT_PROMPT
from src.llm import llm
from src.models import EvaluationResult,InterviewHistoryEntry


def evaluation_agent(state:InterviewState):
    try:
        current_question=state["current_question"]
        current_answer=state["current_answer"]
        question_index=state["question_index"]
        evaluations=state["evaluations"]
        interview_history=state["interview_history"]      
        if state["stop_requested"]:
            logging.info("Interview stopped by user. Skipping evaluation.")       
            return {} 

        if current_question and current_answer and current_answer.strip() != "":
                    prompt =f"""Instructions :
                    {EVALUATION_RESULT_PROMPT}  
                    Question  :
                    {current_question.question}
                    Topic:
                    {current_question.topic}
                    Difficulty :
                    {current_question.difficulty}
                    Candidate answer :
                    {current_answer}"""
                    logging.info("Evaluating the answer")
                    evaluation_llm=llm.with_structured_output(EvaluationResult)
                    response =evaluation_llm.invoke(prompt)      
                    question_index +=1

                    new_evaluation=evaluations +[response]
                    history_entry=InterviewHistoryEntry(
                        question=current_question,
                        answer=current_answer,
                        evaluation=response
                    )
                    new_interview_history=interview_history+[history_entry]
                    return {
                        "evaluations":new_evaluation,
                        "question_index":question_index,
                        "interview_history":new_interview_history,
                        "current_score":response.score,
                        "current_answer":""
                    }
        
    except Exception as e:
        raise CustomException(e,sys)