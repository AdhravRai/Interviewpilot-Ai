from typing import TypedDict
from src.models import InterviewQuestion,TopicPlan,EvaluationResult,FeedbackResult,InterviewHistoryEntry

class InterviewState(TypedDict):
    """ 
    A TypedDict representing the state of the application.
    """
    
    resume_text:str # resume
    skills:list[str]
    projects:list[dict]
    technologies:list[str]
   
    candidate_role: str
    experience_level: str
    weak_areas: list[str]

    interview_plan: list[TopicPlan]
    # Qustions
    questions: list[InterviewQuestion]
    
    # Active interview
    current_question: InterviewQuestion
    current_answer: str
    question_index: int
    
    evaluations: list[EvaluationResult]
    current_score: int
    difficulty_level: str
    
    feedback: FeedbackResult
    interview_history: list[InterviewHistoryEntry]
    roadmap: list[str]
    
    
    