import streamlit as st
from golf_predictor import GolfPredictor

st.set_page_config(page_title='Golf Score Predictor')
st.title('Golf Score Predictor')
st.write('Enter your typical statistics to estimate your score for an 18-hole round.')
with st.form('golf_stats'):
    distance = st.number_input('Average driving distance (yards)', 100, 350, 230)
    fairways = st.number_input('Fairways hit', 0, 14, 6)
    greens = st.number_input('Greens in regulation', 0, 18, 4)
    putts = st.number_input('Total putts', 18, 60, 36)
    handicap = st.number_input('Golf handicap (negative for plus handicap)', -5.0, 54.0, 25.0, step=0.1)
    submitted = st.form_submit_button('Predict Score')
if submitted:
    predictor = GolfPredictor()
    score = predictor.predict(distance, fairways, greens, putts, handicap)
    st.success(f'Predicted 18-hole score: {score}')
st.caption('Prototype trained on synthetic data. Estimates are for demonstration only, assuming a typical par-72 course.')
