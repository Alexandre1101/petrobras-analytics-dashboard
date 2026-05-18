import streamlit as st

from utils.load_data import load_data
from utils.kpis import financial_kpis
from utils.charts import revenue_chart, profit_vs_ebitda_chart, dividends_chart

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Financial Performance Overview",
    page_icon="📈",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

data = load_data()

financeiro = data["financeiro"]

# =========================================================
# PAGE TITLE
# =========================================================
st.image(
    "assets/logo.png",
    width=140
)
st.title("📈 Financial Performance Overview")

st.markdown("""
Strategic financial dashboard analyzing fictional revenue trajectories, 
bottom-line profitability, and capital allocation through dividends.
""")

st.divider()

# =========================================================
# KPIs
# =========================================================

kpi_data = financial_kpis(financeiro)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Revenue",
    value=f"R$ {kpi_data['receita']:.2f} Bi",
    delta=f"{kpi_data['receita_delta']:.1f}%"
)

col2.metric(
    label="Net Profit",
    value=f"R$ {kpi_data['lucro']:.2f} Bi",
    delta=f"{kpi_data['lucro_delta']:.1f}%"
)

col3.metric(
    label="EBITDA",
    value=f"R$ {kpi_data['ebitda']:.2f} Bi",
    delta=f"{kpi_data['ebitda_delta']:.1f}%"
)

col4.metric(
    label="Dividends",
    value=f"R$ {kpi_data['dividendos']:.2f} Bi",
    delta=f"{kpi_data['dividendos_delta']:.1f}%"
)

st.divider()

# =========================================================
# FILTERS
# =========================================================

st.sidebar.markdown("### Period Filters")

anos = financeiro["ano"].unique()

ano_inicial, ano_final = st.sidebar.select_slider(
    "Select Period",
    options=anos,
    value=(anos.min(), anos.max())
)

financeiro_filtrado = financeiro[
    (financeiro["ano"] >= ano_inicial)
    & (financeiro["ano"] <= ano_final)
]

st.divider()

# =========================================================
# MAIN CHART - REVENUE
# =========================================================
st.subheader("Revenue Trajectory")
fig_receita = revenue_chart(financeiro_filtrado)
st.plotly_chart(
    fig_receita,
    use_container_width=True
)

# =========================================================
# SECONDARY CHARTS
# =========================================================
col5, col6 = st.columns(2)

# ---------------------------------------------------------
# PROFIT VS EBITDA
# ---------------------------------------------------------

with col5:
    fig_profit = profit_vs_ebitda_chart(financeiro_filtrado)
    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )

# ---------------------------------------------------------
# DIVIDENDS
# ---------------------------------------------------------

with col6:
    fig_dividendos = dividends_chart(financeiro_filtrado)
    st.plotly_chart(
        fig_dividendos,
        use_container_width=True
    )

st.divider()

# =========================================================
# ANALYTICAL INSIGHTS
# =========================================================

st.subheader("Financial Performance Insights")

receita_media = financeiro_filtrado["receita_bilhoes"].mean()
lucro_medio = financeiro_filtrado["lucro_bilhoes"].mean()

st.info(f"""
Average revenue during the selected period was
R$ {receita_media:.2f} Bi, while average net profit reached
R$ {lucro_medio:.2f} Bi.
""")

# =========================================================
# DATA TABLE
# =========================================================

st.markdown("## Financial Data Table")

st.dataframe(
    financeiro_filtrado,
    use_container_width=True
)