import uuid

from langgraph.types import Command

from src.graph.graph import interview_graph
from src.state import InterviewState


class InterviewApplication:

    def __init__(self):
        self.graph = interview_graph

    def start_interview(self, resume_path: str):

        config = {
            "configurable": {
                "thread_id": str(uuid.uuid4())
            }
        }

        initial_state: InterviewState = {
            "resume_path": resume_path,
            "resume_text": "",

            "skills": [],
            "projects": [],
            "technologies": [],

            "candidate_role": "",
            "experience_level": "",
            "weak_areas": [],
            "interview_plan": [],

            "questions": [],

            "current_question": None,
            "current_answer": "",
            "question_index": 0,
    
            "evaluations": [],
            "current_score": 0,

        
            "difficulty_level": "",
            "feedback": None,
            "roadmap": [],

            "interview_history": [],
        }

        state = self.graph.invoke(
            initial_state,
            config=config,
        )

        return state, config

    def resume_interview(self, config, answer: str):

        state = self.graph.invoke(
            Command(resume=answer),
            config=config,
        )

        return state
    def start_interview(self, resume_path: str):
        pass
