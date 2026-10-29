from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Estoque LCI e LCA", layout="wide")
# tira o espaço padrão do Streamlit em volta da página
st.markdown("<style>.block-container{padding-top:1rem;padding-bottom:0}</style>", unsafe_allow_html=True)

st.iframe(Path(__file__).parent / "LCI_LCA_por_banco.html", height=1000)
