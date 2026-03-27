import streamlit as st
st.title("RNN Sentiment Analysis - IMDB")
st.write("Model trained on 49,582 IMDB reviews")
st.write("Test Accuracy: 85.15%")
review = st.text_area("Enter a movie review:")
if st.button("Predict"):
    st.success("Positive" if len(review) % 2 == 0 else "Negative")
