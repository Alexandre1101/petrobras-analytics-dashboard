import streamlit as st

def load_css():

    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
st.set_page_config(
    page_title="Petrobras Dashboard",
    page_icon="⛽",
    layout="wide"
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.markdown("## Petrobras Analytics")

st.sidebar.markdown("""
Interactive dashboard for fictional Petrobras
financial, operational and ESG analysis.
""")

# =========================================================
# MAIN PAGE
# =========================================================

st.title("⛽ Petrobras Analytics Dashboard")

st.markdown("""
Business intelligence dashboard developed with
Streamlit, Pandas and Plotly.
""")