import streamlit as st
import plotly.express as px
import pandas as pd

from modules.predictor import predict_career
from modules.salary_simulator import salary_growth
from modules.roadmap import generate_roadmap
from modules.ai_chat import ask_ai

st.set_page_config(
    page_title="SkillMirror AI",
    layout="wide"
)

st.title("🚀 SkillMirror AI")
st.subheader("AI Career Simulation Platform")

st.sidebar.title("Skill Inputs")

python_skill = st.sidebar.slider("Python Skill", 1, 10, 5)
ml_skill = st.sidebar.slider("ML Skill", 1, 10, 5)
communication = st.sidebar.slider("Communication", 1, 10, 5)
projects = st.sidebar.slider("Projects", 1, 10, 5)

# Career Prediction
if st.button("Predict My Career"):

    role = predict_career(
        python_skill,
        ml_skill,
        communication,
        projects
    )

    st.success(f"Recommended Career: {role}")

    # Salary Growth
    growth = salary_growth(role)

    df = pd.DataFrame({
        "Year": list(growth.keys()),
        "Salary": list(growth.values())
    })

    fig = px.line(
        df,
        x="Year",
        y="Salary",
        markers=True,
        title="Future Salary Growth"
    )

    st.plotly_chart(fig)

    # Roadmap
    st.subheader("📚 AI Career Roadmap")

    roadmap = generate_roadmap(role)

    st.write(roadmap)

# AI Mentor
st.subheader("🤖 AI Career Mentor")

question = st.text_input(
    "Ask Career Question"
)

if st.button("Ask AI Mentor"):

    answer = ask_ai(question)

    st.write(answer)
