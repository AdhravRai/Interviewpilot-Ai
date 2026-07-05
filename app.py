from src.graphs.graph import interview_graph
from src.state import InterviewState


def create_initial_state(resume_text: str) -> InterviewState:
    """
    Creates the initial shared state for the interview workflow.
    """

    return InterviewState(
        resume_text=resume_text,

        # Resume Analysis
        candidate_role="",
        skills=[],
        projects=[],
        technologies=[],

        # Skill Gap
        weak_areas=[],

        # Planning
        interview_plan=[],

        # Question Generation
        questions=[],

        # Interview
        current_question=None,
        current_answer="",
        question_index=0,

        # Evaluation
        evaluations=[],
        interview_history=[],
        current_score=0.0,

        # Difficulty
        difficulty_level="Medium",

        # Feedback
        feedback=None,

        # Roadmap
        roadmap=None,
    )


def main():

    print("=" * 60)
    print("InterviewPilot AI")
    print("=" * 60)

    resume_text = input("\nPaste the resume text:\n\n")

    initial_state = create_initial_state(resume_text)

    final_state = interview_graph.invoke(initial_state)

    print("\nInterview completed.\n")

    print(final_state)


if __name__ == "__main__":
    main()