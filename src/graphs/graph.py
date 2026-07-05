from langgraph.graph import START,StateGraph,END
from src.state import InterviewState
from src.agents.resume_agent import resume_agent
from src.agents.skill_gap_agent import skill_gap_agent
from src.agents.roadmap_agent import roadmap_agent
from src.agents.question_generator_agent import question_generator
from src.agents.interview_plan_agent import interview_plan_agent
from src.agents.interview_agent import interview_agent
from src.agents.feedback_agent import feedback_agent
from src.agents.evaluation_agent import evaluation_agent
from src.agents.diff_adaptation_agent import difficulty_adaptation_agent


from pathlib import Path

graph=StateGraph(InterviewState)

graph.add_node("resume_analysis",resume_agent)
graph.add_node("skill_gap",skill_gap_agent)
graph.add_node("interview_planner",interview_plan_agent)
graph.add_node("interview",interview_agent)
graph.add_node("question_generator",question_generator)
graph.add_node("evaluation",evaluation_agent)
graph.add_node("difficulty_adaptation",difficulty_adaptation_agent)
graph.add_node("feedback",feedback_agent)
graph.add_node("roadmap",roadmap_agent)

graph.add_edge(START,"resume_analysis")
graph.add_edge("resume_analysis","skill_gap")
graph.add_edge("skill_gap","interview_planner")
graph.add_edge("interview_planner","question_generator")
graph.add_edge("question_generator","interview")
graph.add_edge("interview", "evaluation")
graph.add_edge("evaluation", "difficulty_adaptation")

def route_after_adaptation(state: InterviewState):
    question_index = state["question_index"]
    questions = state["questions"]

    if question_index < len(questions):
        return "interview"

    return "feedback"

graph.add_conditional_edges("difficulty_adaptation",
                             route_after_adaptation,
    {
        "interview": "interview",
        "feedback": "feedback",
    },
)
graph.add_edge("feedback","roadmap")
graph.add_edge("roadmap",END)

interview_graph = graph.compile()

def save_graph():
    artifact_dir = Path("artifacts") / "graph"
    artifact_dir.mkdir(parents=True, exist_ok=True)
    png = interview_graph.get_graph().draw_mermaid_png()

    with open(artifact_dir / "interview_graph.png", "wb") as f:
        f.write(png)



if __name__ == "__main__":
    save_graph()