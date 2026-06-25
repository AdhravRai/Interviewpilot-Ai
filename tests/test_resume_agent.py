from src.agents.resume_agent import resume_agent

dummy_state = {
    "resume_text": """
    Python Developer
    Skills: Python, Machine Learning, Docker
    Project: Salary Prediction System
    """
}

response = resume_agent(dummy_state)

print(response.content)
print(type(response))