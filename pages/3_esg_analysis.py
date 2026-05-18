import streamlit as st
import plotly.express as px

from utils.load_data import load_data

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ESG Analysis",
    page_icon="🌱",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

data = load_data()

esg = data["esg"]

# =========================================================
# TITLE
# =========================================================
st.image(
    "assets/logo.png",
    width=180
)
st.title("🌱 ESG Analysis")

st.markdown("""
Environmental, social and governance indicators dashboard based on fictional Petrobras ESG data.
""")

st.divider()

# =========================================================
# KPIs
# =========================================================

co2 = esg["emissoes_co2_mton"].iloc[-1]
acidentes = esg["acidentes"].sum()
investimento = esg["investimento_ambiental_milhoes"].sum()

col1, col2, col3 = st.columns(3)

col1.metric(
    "CO₂ Emissions",
    f"{co2:.2f} Mt"
)

col2.metric(
    "Operational Incidents",
    f"{acidentes}"
)

col3.metric(
    "Environmental Investment",
    f"R$ {investimento:.2f} M"
)

st.divider()

# =========================================================
# EMISSIONS
# =========================================================

st.markdown("## CO₂ Emissions")

fig1 = px.line(
    esg,
    x="ano",
    y="emissoes_co2_mton",
    markers=True,
    title="CO₂ Emissions Over Time"
)

fig1.update_layout(
    template="plotly_dark",
    xaxis_title="Year",
    yaxis_title="Million Tons"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================================================
# SECONDARY CHARTS
# =========================================================

col4, col5 = st.columns(2)

# ---------------------------------------------------------
# INCIDENTS
# ---------------------------------------------------------

with col4:

    fig2 = px.bar(
        esg,
        x="ano",
        y="acidentes",
        title="Operational Incidents"
    )

    fig2.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Incidents"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------------------------------------------------
# ENVIRONMENTAL INVESTMENTS
# ---------------------------------------------------------

with col5:

    fig3 = px.area(
        esg,
        x="ano",
        y="investimento_ambiental_milhoes",
        title="Environmental Investments"
    )

    fig3.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Million R$"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.divider()

# =========================================================
# ESG INSIGHTS
# =========================================================

media_emissoes = esg["emissoes_co2_mton"].mean()

st.info(f"""
Average CO₂ emissions during the analyzed period were
{media_emissoes:.2f} million tons.
""")

# =========================================================
# DATA TABLE
# =========================================================

st.markdown("## ESG Data Table")

st.dataframe(
    esg,
    use_container_width=True
)