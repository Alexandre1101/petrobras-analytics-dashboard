import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils.load_data import load_data
from utils.kpis import financial_kpis

# =========================================================
# PAGE CONFIG
# =========================================================
st.image(
    "assets/logo.png",
    width=180
)
st.set_page_config(
    page_title="Financial Overview",
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

st.title("📈 Financial Overview")

st.markdown("""
Financial analysis dashboard containing fictional Petrobras revenue,
profitability and dividend indicators.
""")

st.divider()

# =========================================================
# KPIs
# =========================================================

kpis = financial_kpis(financeiro)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Revenue",
    value=f"R$ {kpis['receita']:.2f} Bi",
    delta=f"{kpis['receita_delta']:.1f}%"
)

col2.metric(
    label="Net Profit",
    value=f"R$ {kpis['lucro']:.2f} Bi",
    delta=f"{kpis['lucro_delta']:.1f}%"
)

col3.metric(
    label="EBITDA",
    value=f"R$ {kpis['ebitda']:.2f} Bi",
    delta=f"{kpis['ebitda_delta']:.1f}%"
)

col4.metric(
    label="Dividends",
    value=f"R$ {kpis['dividendos']:.2f} Bi",
    delta=f"{kpis['dividendos_delta']:.1f}%"
)

st.divider()

# =========================================================
# FILTERS
# =========================================================

st.markdown("### Dashboard Filters")

anos = financeiro["ano"].unique()

ano_inicial, ano_final = st.select_slider(
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

st.markdown("## Revenue Evolution")

fig_receita = px.line(
    financeiro_filtrado,
    x="ano",
    y="receita_bilhoes",
    markers=True,
    title="Revenue Over Time"
)

fig_receita.update_layout(
    xaxis_title="Year",
    yaxis_title="Revenue (Billion R$)",
    template="plotly_dark"
)

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

    fig_profit = go.Figure()

    fig_profit.add_trace(
        go.Bar(
            x=financeiro_filtrado["ano"],
            y=financeiro_filtrado["lucro_bilhoes"],
            name="Net Profit"
        )
    )

    fig_profit.add_trace(
        go.Bar(
            x=financeiro_filtrado["ano"],
            y=financeiro_filtrado["ebitda_bilhoes"],
            name="EBITDA"
        )
    )

    fig_profit.update_layout(
        title="Profit vs EBITDA",
        barmode="group",
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Billion R$"
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )

# ---------------------------------------------------------
# DIVIDENDS
# ---------------------------------------------------------

with col6:

    fig_dividendos = px.area(
        financeiro_filtrado,
        x="ano",
        y="dividendos_bilhoes",
        title="Dividends Distribution"
    )

    fig_dividendos.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Dividends (Billion R$)"
    )

    st.plotly_chart(
        fig_dividendos,
        use_container_width=True
    )

st.divider()

# =========================================================
# ANALYTICAL INSIGHTS
# =========================================================

st.markdown("## Financial Insights")

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