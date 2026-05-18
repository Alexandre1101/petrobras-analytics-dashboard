import streamlit as st
import os

# st.set_page_config MUST be the first Streamlit command
st.set_page_config(
    page_title="Petrobras Intelligence Dashboard",
    page_icon="⛽",
    layout="wide"
)

def load_css():
    css_path = "assets/style.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_sidebar():
    st.sidebar.image("assets/logo.png", use_container_width=True)
    st.sidebar.title("Petrobras Intelligence")
    st.sidebar.markdown("""
    ---
    **Strategic Analytics Interface**  
    Advanced monitoring of financial, operational, and ESG performance indicators.
    """)
    st.sidebar.caption("Fictional Educational Data Project")

load_css()
render_sidebar()

# =========================================================
# MAIN LANDING PAGE
# =========================================================

st.title("⛽ Corporate Performance Dashboard")

st.markdown("""
Welcome to the **Petrobras Strategic Intelligence Suite**. This application provides a 
high-fidelity overview of corporate health through four specialized analytical pillars.
""")

col1, col2 = st.columns(2)

with col1:
    st.info("👈 Use the **Sidebar** to navigate between specialized reports.")
    
with col2:
    st.success("""
    **Key Features:**
    - Real-time KPI Calculation
    - Multi-dimensional Production Filtering
    - ESG Sustainability Tracking
    - Market Intelligence Visuals
    """)