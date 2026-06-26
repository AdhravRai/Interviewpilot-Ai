from typing import TypedDict

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

    interview_plan: dict[str,int]
    # Qustions
    questions: list[str]

    # Active interview
    current_question: str
    current_answer: str
    question_index: int
    
    evaluations: list[dict]
    score: float
    difficulty_level: str

    feedback: str
    roadmap: list[str]
    interview_history: list[dict]
    
    
    