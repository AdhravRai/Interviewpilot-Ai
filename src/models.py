from pydantic import BaseModel

#Every agent gets its own output model in this files stored.Tell the agent type of output
class ResumeAnalysis(BaseModel):
    skills:list[str]
    projects:list[dict]
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
