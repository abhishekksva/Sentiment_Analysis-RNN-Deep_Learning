# RNN Sentiment Analysis - IMDB Reviews (PyTorch)

## Overview
Classifies IMDB movie reviews as Positive or Negative using a Recurrent Neural Network.

## Dataset
- 49,582 IMDB reviews
- Binary labels: Positive / Negative

## Tech Stack
- Python, Pandas, PyTorch
- Scikit-learn (TF-IDF)
- Streamlit

## Architecture
- TF-IDF Vectorizer (5000 features)
- RNN with 128 hidden units
- Binary Cross Entropy Loss

## Results
- Test Accuracy: 85.15%

## How to Run
pip install -r requirements.txt
streamlit run app.py

### Streamlit app Link
https://abhishekksva-sentiment-analysis-rnn-deep-learning-app-z2c9na.streamlit.app/
