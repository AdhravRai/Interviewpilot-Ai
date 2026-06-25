from pydantic import BaseModel

#Every agent gets its own output model in this files stored.Tell the agent type of output
class ResumeAnalysis(BaseModel):
    skills:list[str]
    projects:list[dict]
    technologies:list[str]
    candidate_role:str
    experience_level:str