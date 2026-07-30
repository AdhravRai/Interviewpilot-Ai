# 🎯 InterviewPilot AI

Live link : https://interviewpilot-ai-a3je.onrender.com

> **A Multi-Agent Interview Preparation Platform built with LangGraph, LangChain, Gemini, Streamlit, and LangSmith.**

InterviewPilot AI simulates a technical interview using multiple AI agents that collaborate through a shared state. Instead of generating isolated interview questions, the system analyzes a candidate's resume, identifies skill gaps, plans a personalized interview, evaluates answers, adapts difficulty dynamically, and generates actionable feedback with a personalized learning roadmap.

---

## 🚀 Features

- 📄 Resume Analysis using LLM
- 🧠 Skill Gap Detection
- 📋 Personalized Interview Planning
- ❓ Dynamic Question Generation
- 👨‍💻 Human-in-the-loop Interview using LangGraph Interrupts
- 📊 Answer Evaluation
- 📈 Adaptive Difficulty Adjustment
- 📝 Detailed Interview Feedback
- 📚 Personalized Learning Roadmap
- 💾 Persistent Conversation State with SQLite Checkpointer
- 🔍 LangSmith Tracing & Observability
- 🌐 Interactive Streamlit Interface

---

# 🏗 Workflow Architecture

<p align="center">
    <img src="artifacts/graph/interview_graph.png" width="900">
</p>

# 🏗 Architecture

```text
                 Resume Upload
                       │
                       ▼
             Resume Analysis Agent
                       │
                       ▼
             Skill Gap Detection Agent
                       │
                       ▼
            Interview Planning Agent
                       │
                       ▼
           Question Generator Agent
                       │
                       ▼
              Interview Agent
        (Human-in-the-loop Interrupt)
                       │
             User submits answer
                       │
                       ▼
              Evaluation Agent
                       │
                       ▼
        Difficulty Adaptation Agent
                       │
             More Questions?
             ┌──────────────┐
             │              │
            Yes            No
             │              │
             ▼              ▼
       Interview Agent   Feedback Agent
                               │
                               ▼
                       Roadmap Agent
                               │
                               ▼
                              END
```

---

# 🤖 Multi-Agent Workflow

## 1️⃣ Resume Analysis Agent

- Extracts resume text
- Identifies skills
- Extracts projects
- Detects technologies

---

## 2️⃣ Skill Gap Agent

Analyzes the candidate profile and predicts potential weak interview areas.

Example:

- System Design
- MLOps
- SQL

---

## 3️⃣ Interview Planner Agent

Creates a personalized interview plan based on:

- Resume
- Skills
- Projects
- Experience level

---

## 4️⃣ Question Generator Agent

Generates interview questions aligned with the interview plan.

Each question contains:

- Topic
- Difficulty
- Question

---

## 5️⃣ Interview Agent

Handles the interview session using LangGraph's Human-in-the-Loop interrupt.

The user can:

- Submit Answer
- End Interview

---

## 6️⃣ Evaluation Agent

Evaluates each answer using the LLM.

Returns:

- Score
- Strengths
- Weaknesses
- Explanation

---

## 7️⃣ Difficulty Adaptation Agent

Adjusts interview difficulty dynamically based on previous performance.

Example:

- Strong performance → Harder questions
- Weak performance → Easier questions

---

## 8️⃣ Feedback Agent

Generates:

- Interview Summary
- Strengths
- Areas of Improvement
- Final Assessment

---

## 9️⃣ Roadmap Agent

Creates a personalized learning roadmap prioritizing weak concepts.

---

# 🧠 Shared State

All agents communicate through a shared LangGraph state.

```python
InterviewState = {
    "resume_text": "",
    "skills": [],
    "projects": [],
    "technologies": [],
    "weak_areas": [],
    "interview_plan": [],
    "questions": [],
    "current_question": {},
    "current_answer": "",
    "evaluations": [],
    "difficulty_level": "",
    "feedback": {},
    "roadmap": {}
}
```

This shared state enables loose coupling between agents and makes the workflow modular and scalable.

---

# ⚙ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Agent Framework | LangGraph |
| LLM Framework | LangChain |
| LLM | Google Gemini |
| UI | Streamlit |
| State Management | LangGraph StateGraph |
| Checkpointing | SQLite Checkpointer |
| Observability | LangSmith |
| Resume Parsing | PyMuPDF |
| Validation | Pydantic |

---

# 📂 Project Structure

```text
interview-pilot/

│
├── app.py
├── streamlit_app.py
│
├── src/
│
├── agents/
│   ├── resume_agent.py
│   ├── skill_gap_agent.py
│   ├── interview_plan_agent.py
│   ├── question_generator_agent.py
│   ├── interview_agent.py
│   ├── evaluation_agent.py
│   ├── diff_adaptation_agent.py
│   ├── feedback_agent.py
│   └── roadmap_agent.py
│
├── prompts/
│
├── models.py
├── state.py
├── llm.py
├── logger.py
├── exceptions.py
│
└── graphs/
    └── graph.py
```

---

# ▶ Running Locally

## Clone Repository

```bash
git clone https://github.com/AdhravRai/interview-pilot.git
```

```bash
cd interview-pilot
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key

LANGSMITH_API_KEY=your_langsmith_key

LANGSMITH_TRACING=true

LANGSMITH_PROJECT=InterviewPilot-AI
```

---

## Run Application

```bash
streamlit run streamlit_app.py
```

---

# 📊 LangSmith Observability

The project integrates LangSmith for production-grade tracing.

It provides:

- Agent execution tracking
- Prompt inspection
- LLM responses
- Token usage
- Latency monitoring
- Workflow visualization

---

# 🎯 Example Workflow

```text
Upload Resume
        │
        ▼
Resume Analysis
        │
        ▼
Skill Gap Detection
        │
        ▼
Interview Planning
        │
        ▼
Question Generation
        │
        ▼
Interview Begins
        │
        ▼
Answer Evaluation
        │
        ▼
Difficulty Adaptation
        │
        ▼
Interview Feedback
        │
        ▼
Learning Roadmap
```

---

# 🔮 Future Improvements

- 🎤 Voice Interview using Vapi
- 📈 Performance Dashboard
- 📄 Interview Report PDF
- 🏢 Company-specific Interview Modes
- 🌍 Multi-language Interviews
- 📹 Webcam & Communication Analysis
- 📊 Historical Interview Analytics

---

# 📸 Demo

### Home Screen

![Home Screen](artifacts/Home.png)

### Interview Session

![Interview](artifacts/Interviewpage.png)

### Feedback

![Feedback](artifacts/feedback.png)

### LangSmith Tracing

![LangSmith](artifacts/Langsmithtracing.png)

---

# 💡 Key Concepts Demonstrated

- Multi-Agent Orchestration
- Human-in-the-Loop Workflows
- Shared State Management
- Agent Communication
- Adaptive AI Systems
- LLM Evaluation
- Workflow Orchestration
- Production AI Architecture
- Observability with LangSmith

---

# 👨‍💻 Author

**Adhrav Rai**

- GitHub: https://github.com/AdhravRai
- LinkedIn:(https://www.linkedin.com/in/adhrav-rai-8b2991327/)

---

## ⭐ If you found this project helpful, consider giving it a star!
