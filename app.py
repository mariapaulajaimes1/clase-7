import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# Estilo general con CSS
st.markdown(
    """
    <style>
    .title {
        color: #6C63FF;
        font-size: 40px;
        font-weight: bold;
    }
    .subtitle {
        color: #2C3E50;
        font-size: 24px;
        font-weight: bold;
    }
    .description {
        color: #34495E;
        font-size: 18px;
    }
    .result-positive {
        color: #27AE60;
        font-size: 20px;
        font-weight: bold;
    }
    .result-neutral {
        color: #F1C40F;
        font-size: 20px;
        font-weight: bold;
    }
    .result-negative {
        color: #E74C3C;
        font-size: 20px;
        font-weight: bold;
    }
    .sidebar-text {
        color: #2980B9;
        font-size: 16px;
    }
    </style>
   
