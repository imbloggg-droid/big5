
import streamlit as st
from analyze import analyze_big_five

st.set_page_config(page_title="Big Five Evaluator", layout="wide")

st.title("⚽ Big Five Personality Evaluator")
st.markdown("Analyze football players' personalities from interviews using the Big Five model.")

player_name = st.text_input("Player Name")
interview_text = st.text_area("Paste interview text here", height=300)

if st.button("Evaluate"):
    if player_name and interview_text:
        result = analyze_big_five(interview_text, player_name)

if "error" in result:
    st.error(f"Error: {result['error']}")
elif not isinstance(result, dict):
    st.error("Invalid response format from model.")
else:
    st.subheader("Big Five Scores")
    for trait in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]:
        data = result.get(trait)
        if isinstance(data, dict):
            st.markdown(f"**{trait.capitalize()}**: {data.get('score', '?')}  \n*{data.get('comment', 'No comment')}*")

    st.subheader("Summary")
    st.write(result.get("summary", "No summary provided."))

    st.subheader("JSON Result")
    st.json(result)
