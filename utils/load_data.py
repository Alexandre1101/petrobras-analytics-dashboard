import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    file_path = "data/petrobras_dados_ficticios.xlsx"
    
    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(file_path):
        st.error(f"Arquivo não encontrado: {file_path}. Verifique se a pasta 'data' existe.")
        st.stop()

    try:
        # Usa 'with' para garantir que o recurso seja liberado
        with pd.ExcelFile(file_path) as excel:
            # Verifica se as abas esperadas existem no arquivo
            sheets_no_arquivo = excel.sheet_names
            abas_esperadas = ["producao", "financeiro", "esg", "petr4"]
            
            for aba in abas_esperadas:
                if aba not in sheets_no_arquivo:
                    st.error(f"A aba '{aba}' não foi encontrada no Excel. Abas disponíveis: {sheets_no_arquivo}")
                    st.stop()

            data = {
                "producao": pd.read_excel(excel, "producao"),
                "financeiro": pd.read_excel(excel, "financeiro"),
                "esg": pd.read_excel(excel, "esg"),
                "petr4": pd.read_excel(excel, "petr4")
            }
        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        st.stop()