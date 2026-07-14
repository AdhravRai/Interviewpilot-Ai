from typing import TypedDict
from src.models import InterviewQuestion,TopicPlan,EvaluationResult,FeedbackResult,InterviewHistoryEntry

class InterviewState(TypedDict):
    resume_path:str
    resume_text:str 
    skills:list[str]
    projects:list[dict]
    technologies:list[str]
   
    candidate_role: str
    experience_level: str
    weak_areas: list[str]

    interview_plan: list[TopicPlan]
    questions: list[InterviewQuestion]
    
    current_question: Optional[InterviewQuestion]
    current_answer: str
    question_index: int
    
    evaluations: list[EvaluationResult]
    current_score: int
    difficulty_level: str
    
    feedback: FeedbackResult
    interview_history: list[InterviewHistoryEntry]
    roadmap: list[str]
    
    
    