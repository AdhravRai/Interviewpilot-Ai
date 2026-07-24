import tempfile
import streamlit as st
from app import InterviewApplication

st.set_page_config(
    page_title="InterviewPilot AI",
    page_icon="🎯",
    layout="wide",
)
st.title("🎯 InterviewPilot AI")
st.markdown("### Multi-Agent Interview Preparation Platform")
app = InterviewApplication()

if "config" not in st.session_state:
    st.session_state.config = None
if "graph_state" not in st.session_state:
    st.session_state.graph_state = None

uploaded_resume = st.file_uploader(
    "Upload your Resume",
    type=["pdf"],
)
if uploaded_resume is not None and st.button("Start Interview"):
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf",
    ) as temp_file:

        temp_file.write(uploaded_resume.read())
        resume_path = temp_file.name
    graph_state, config = app.start_interview(resume_path)
    st.session_state.graph_state = graph_state
    st.session_state.config = config
    st.rerun()

if st.session_state.graph_state:
    state = st.session_state.graph_state
    if "__interrupt__" in state:
    
        interrupt_data = state["__interrupt__"][0].value
    
        st.subheader("Interview Question")
    
        st.write(f"**Topic:** {interrupt_data['topic']}")
        st.write(f"**Difficulty:** {interrupt_data['difficulty']}")
    
        st.markdown("---")
        st.write(interrupt_data["question"])
    
        answer = st.text_area(
            "Your Answer",
            key="answer_box",
            height=220,
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            if st.button("Submit Answer", use_container_width=True):
    
                graph_state = app.resume_interview(
                    st.session_state.config,
                    answer,
                )
    
                st.session_state.graph_state = graph_state
    
                # Clear textbox
                st.session_state.answer_box = ""
    
                st.rerun()
    
        with col2:
            if st.button(
                "End Interview",
                type="secondary",
                use_container_width=True,
            ):
    
                graph_state = app.stop_interview(
                    st.session_state.config
                )
    
                st.session_state.graph_state = graph_state
    
                st.session_state.answer_box = ""
    
                st.rerun()
    else:
        st.success("🎉 Interview Completed!")
        feedback = state["feedback"]
        st.header("Interview Feedback")
        st.write(f"### Summary")
        st.write(feedback.summary)
        st.write("### Strengths")
        for item in feedback.strengths:
            st.write(f"✅ {item}")
        st.write("### Improvement Areas")
        for item in feedback.improvement_areas:
            st.write(f"🔹 {item}")
        st.write("### Final Assessment")
        st.info(feedback.final_assessment)

        st.header("Learning Roadmap")
        roadmap = state["roadmap"].roadmap
        for item in roadmap:
            st.write(
                f"📘 **{item.topic}** ({item.priority})"
            )