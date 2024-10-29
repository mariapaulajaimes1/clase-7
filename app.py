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
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🔍 Análisis de Sentimiento</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">✍️ Por favor escribe en el campo de texto la frase que deseas analizar</div>', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('<div class="subtitle">📊 Polaridad y Subjetividad</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="sidebar-text">
        <ul>
            <li><b>Polaridad</b>: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
            Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.</li>
            <li><b>Subjetividad</b>: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo (hechos). 
            Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with st.expander('💬 Análisis de Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('✍️ Escribe tu frase aquí:')
    if text1:
        blob = TextBlob(text1)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('**📈 Polaridad:**', polarity)
        st.write('**📊 Subjetividad:**', subjectivity)

        if polarity >= 0.5:
            st.markdown('<div class="result-positive">Sentimiento Positivo 😊</div>', unsafe_allow_html=True)
        elif polarity <= -0.5:
            st.markdown('<div class="result-negative">Sentimiento Negativo 😔</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-neutral">Sentimiento Neutral 😐</div>', unsafe_allow_html=True)

with st.expander('🔍 Corrección en inglés'):
    text2 = st.text_area('✍️ Escribe tu texto en inglés aquí:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write('**📝 Corrección:**', blob2.correct())
