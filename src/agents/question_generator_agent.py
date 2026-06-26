import sys
from src.models import QuestionGenerationResult
from src.prompts.question_generation_prompt import QUESTION_GENERATOR_PROMPT
from src.state import InterviewState
from src.llm import llm
from src.logger import logging
from src.exceptions import CustomException

def question_generator(state:InterviewState):
    try:
      if not state["interview_plan"]:
        raise ValueError("Interview plan is empty")        
      interviewplan={
        "starting_difficulty":state["difficulty_level"],
        "plan":state["interview_plan"]
      }
      prompt=f"""
      Question generation instructions :
      {QUESTION_GENERATOR_PROMPT}
      Interview Plan :
      {interviewplan}
  
      """
      structured_llm=llm.with_structured_output(QuestionGenerationResult)
      logging.info("Question Generator Agent start")      
      result=structured_llm.invoke(prompt)
      logging.info("Question Generation completed successfully ")
      return {
          "questions":result.questions
      }    
    except Exception as e:
        raise CustomException(e,sys)     
