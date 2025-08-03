# app.py

import streamlit as st
from scoring import score_answer
from feedback import generate_feedback
from interview_engine import get_question
from voice_input import listen
from voice_output import speak

st.set_page_config(page_title="InterviewPro AI", layout="centered")
st.title(" InterviewPro AI  Voice-Based Interview Coach")

# Select role and level
role = st.selectbox("Select Role:", ["Software Engineer", "Data Scientist", "ML Engineer"])
level = st.selectbox("Experience Level:", ["Entry-Level", "Mid-Level", "Senior"])

# Session state for multi-question flow
if "step" not in st.session_state:
    st.session_state.step = 0
if "history" not in st.session_state:
    st.session_state.history = []
if "question" not in st.session_state:
    st.session_state.question = get_question(role, level, 0)

# Show current question
st.info(f"Question {st.session_state.step + 1}: {st.session_state.question}")

# Button to start recording voice answer
if st.button(" Start Recording"):
    with st.spinner("Listening to your answer..."):
        user_answer = listen()
        st.success("Captured your answer!")

        # Optional: playback the audio
        st.audio("response.wav")

        # Analyze the answer
        score, details = score_answer(user_answer)
        feedback = generate_feedback(user_answer, score, details)

        # Store history
        st.session_state.history.append({
            "question": st.session_state.question,
            "answer": user_answer,
            "score": score,
            "feedback": feedback
        })

        # Show feedback
        st.subheader(" Your Score")
        st.json(score)

        st.subheader(" Feedback")
        st.write(feedback)

        speak("Here's your feedback: " + feedback)

        # Load next question
        st.session_state.step += 1
        st.session_state.question = get_question(role, level, st.session_state.step)

# Show full history of the mock interview
if st.session_state.history:
    with st.expander(" Interview History"):
        for i, item in enumerate(st.session_state.history):
            st.markdown(f"**Q{i+1}:** {item['question']}")
            st.markdown(f"**Answer:** {item['answer']}")
            st.markdown(f"**Score:** {item['score']}")
            st.markdown(f"**Feedback:** {item['feedback']}")
            st.markdown("---")
