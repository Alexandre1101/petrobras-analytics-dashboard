import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils.load_data import load_data

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Production Analysis",
    page_icon="🛢️",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

data = load_data()

producao = data["producao"]

# =========================================================
# TITLE
# =========================================================

st.title("🛢️ Production Analysis")

st.markdown("""
Operational dashboard focused on fictional oil and gas production data.
""")

st.divider()

# =========================================================
# KPIs
# =========================================================

total_petroleo = producao["petroleo_barris_dia"].sum()
media_petroleo = producao["petroleo_barris_dia"].mean()
total_gas = producao["gas_milhoes_m3"].sum()
regioes = producao["regiao"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Oil Production",
    f"{total_petroleo:,.0f}"
)

col2.metric(
    "Average Production",
    f"{media_petroleo:,.0f}"
)

col3.metric(
    "Natural Gas",
    f"{total_gas:,.0f} Mm³"
)

col4.metric(
    "Operating Regions",
    f"{regioes}"
)

st.divider()

# =========================================================
# FILTERS
# =========================================================

st.markdown("### Dashboard Filters")

regiao = st.multiselect(
    "Select Regions",
    producao["regiao"].unique(),
    default=producao["regiao"].unique()
)

producao_filtrada = producao[
    producao["regiao"].isin(regiao)
]

st.divider()

# =========================================================
# OIL PRODUCTION OVER TIME
# =========================================================

st.markdown("## Oil Production Evolution")

fig1 = px.line(
    producao_filtrada,
    x="ano",
    y="petroleo_barris_dia",
    color="regiao",
    markers=True,
    title="Oil Production by Region"
)

fig1.update_layout(
    template="plotly_dark",
    xaxis_title="Year",
    yaxis_title="Barrels per Day"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================================================
# SECONDARY CHARTS
# =========================================================

col5, col6 = st.columns(2)

# ---------------------------------------------------------
# GAS PRODUCTION
# ---------------------------------------------------------

with col5:

    fig2 = px.bar(
        producao_filtrada,
        x="regiao",
        y="gas_milhoes_m3",
        color="regiao",
        title="Natural Gas Production"
    )

    fig2.update_layout(
        template="plotly_dark",
        xaxis_title="Region",
        yaxis_title="Million m³"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------------------------------------------------
# REGIONAL SHARE
# ---------------------------------------------------------

with col6:

    regional = (
        producao_filtrada
        .groupby("regiao")["petroleo_barris_dia"]
        .sum()
        .reset_index()
    )

    fig3 = px.pie(
        regional,
        names="regiao",
        values="petroleo_barris_dia",
        title="Production Share by Region"
    )

    fig3.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.divider()

# =========================================================
# DATA TABLE
# =========================================================

st.markdown("## Production Data Table")

st.dataframe(
    producao_filtrada,
    use_container_width=True
)