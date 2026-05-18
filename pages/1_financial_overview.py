import streamlit as st
from utils.load_data import load_data
from utils.charts import revenue_chart
from utils.kpis import financial_kpis


st.title("📈 Financial Overview")

data = load_data()

financeiro = data["financeiro"]

fig = revenue_chart(financeiro)

st.plotly_chart(fig, use_container_width=True)

# calculando KPIs
(
    receita,
    lucro,
    ebitda,
    receita_delta,
    lucro_delta,
    ebitda_delta
) = financial_kpis(financeiro)

# criando colunas
col1, col2, col3 = st.columns(3)

# exibindo KPIs
col1.metric(
    "Receita",
    f"R$ {receita:.2f} Bi",
    delta=f"{receita_delta:.1f}%"
)

col2.metric(
    "Lucro",
    f"R$ {lucro:.2f} Bi",
    delta=f"{lucro_delta:.1f}%"
)

col3.metric(
    "EBITDA",
    f"R$ {ebitda:.2f} Bi",
    delta=f"{ebitda_delta:.1f}%"
)