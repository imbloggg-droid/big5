
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
        st.subheader("Big Five Scores")
        for trait, data in result.items():
            if trait not in ["player", "summary"]:
                st.markdown(f"**{trait.capitalize()}**: {data['score']}  
*{data['comment']}*")
        st.subheader("Summary")
        st.write(result["summary"])
        st.subheader("JSON Result")
        st.json(result)
    else:
        st.warning("Please enter both player name and interview text.")
