import streamlit as st
from utils.load_data import load_data

st.set_page_config(
    page_title="Petrobras Dashboard",
    page_icon="⛽",
    layout="wide"
)

st.title("⛽ Petrobras Analytics Dashboard")

data = load_data()

st.subheader("Prévia dos Dados Financeiros")

st.dataframe(data["financeiro"])