from pydantic import BaseModel

#Every agent gets its own output model in this files stored.Tell the agent type of output
class ResumeAnalysis(BaseModel):
    skills:list[str]
    projects:list[str]
    technologies:list[str]
    candidate_role:str
    experience_level:str

class SkillGapResult(BaseModel):
    weak_areas:list[str]
    reasoning:str
class TopicPlan(BaseModel):
    topic:str
    questions:int
    priority:str
class InterviewPlanner(BaseModel):
    starting_difficulty:str
    interview_topics:list[TopicPlan]

class InterviewQuestion(BaseModel):
    topic:str
    question:str
    difficulty:str
class QuestionGenerationResult(BaseModel):
    questions: list[InterviewQuestion]

class EvaluationResult(BaseModel):
    score:int   
    strengths:list[str]    
    weaknesses:list[str]    
    missing_concepts:list[str]    
    feedback:str

class InterviewHistoryEntry(BaseModel):
    question: InterviewQuestion
    answer: str
    evaluation: EvaluationResult
class DifficultyAdaptationResult(BaseModel):
    difficulty_level:str
    reasoning:str

class FeedbackResult(BaseModel):
    summary:str
    strengths:list[str]
    improvement_areas:list[str]
    final_assessment:str
class RoadmapItem(BaseModel):
    topic: str
    priority: str
class RoadmapResult(BaseModel):
    roadmap: list[RoadmapItem]

    