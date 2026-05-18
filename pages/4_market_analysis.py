import streamlit as st
import plotly.express as px

from utils.load_data import load_data

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Market Analysis",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

data = load_data()

petr4 = data["petr4"]

# =========================================================
# TITLE
# =========================================================

st.title("📊 Market Analysis")

st.markdown("""
Financial market dashboard focused on fictional PETR4 stock indicators.
""")

st.divider()

# =========================================================
# KPIs
# =========================================================

preco = petr4["preco_medio"].iloc[-1]
volume = petr4["volume_medio_milhoes"].iloc[-1]
dy = petr4["dividend_yield"].iloc[-1]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Price",
    f"R$ {preco:.2f}"
)

col2.metric(
    "Trading Volume",
    f"{volume:.2f} M"
)

col3.metric(
    "Dividend Yield",
    f"{dy:.2f}%"
)

st.divider()

# =========================================================
# PRICE EVOLUTION
# =========================================================

st.markdown("## PETR4 Price Evolution")

fig1 = px.line(
    petr4,
    x="ano",
    y="preco_medio",
    markers=True,
    title="Average Stock Price"
)

fig1.update_layout(
    template="plotly_dark",
    xaxis_title="Year",
    yaxis_title="Price (R$)"
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
# TRADING VOLUME
# ---------------------------------------------------------

with col4:

    fig2 = px.bar(
        petr4,
        x="ano",
        y="volume_medio_milhoes",
        title="Trading Volume"
    )

    fig2.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Million Shares"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------------------------------------------------
# DIVIDEND YIELD
# ---------------------------------------------------------

with col5:

    fig3 = px.area(
        petr4,
        x="ano",
        y="dividend_yield",
        title="Dividend Yield Evolution"
    )

    fig3.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="%"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.divider()

# =========================================================
# DATA TABLE
# =========================================================

st.markdown("## Market Data Table")

st.dataframe(
    petr4,
    use_container_width=True
)