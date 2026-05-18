import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# CHART STYLING CONSTANTS
# =========================================================
CHART_TEMPLATE = "plotly_dark"

def apply_layout(fig, title, x_title="", y_title=""):
    fig.update_layout(
        title=f"<b>{title}</b>",
        template=CHART_TEMPLATE,
        xaxis_title=x_title,
        yaxis_title=y_title,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

# =========================================================
# FINANCIAL CHARTS
# =========================================================

def revenue_chart(df):
    fig = px.line(df, x="ano", y="receita_bilhoes", markers=True)
    return apply_layout(fig, "Revenue Evolution", "Fiscal Year", "Billion R$")

def profit_vs_ebitda_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["ano"], y=df["lucro_bilhoes"], name="Net Profit"))
    fig.add_trace(go.Bar(x=df["ano"], y=df["ebitda_bilhoes"], name="EBITDA"))
    fig.update_layout(barmode="group")
    return apply_layout(fig, "Profitability Comparison", "Fiscal Year", "Billion R$")

def dividends_chart(df):
    fig = px.area(df, x="ano", y="dividendos_bilhoes")
    return apply_layout(fig, "Dividend Distribution Strategy", "Fiscal Year", "Billion R$")

# =========================================================
# PRODUCTION CHARTS
# =========================================================

def oil_production_chart(df):
    fig = px.line(df, x="ano", y="petroleo_barris_dia", color="regiao", markers=True)
    return apply_layout(fig, "Oil Production Evolution", "Year", "Barrels per Day")

def gas_production_chart(df):
    fig = px.bar(df, x="regiao", y="gas_milhoes_m3", color="regiao")
    return apply_layout(fig, "Natural Gas Output by Region", "Geographic Area", "Million m³")

def regional_share_chart(df):
    regional = df.groupby("regiao")["petroleo_barris_dia"].sum().reset_index()
    fig = px.pie(regional, names="regiao", values="petroleo_barris_dia", hole=0.4)
    return apply_layout(fig, "Operational Share per Region")

# =========================================================
# ESG CHARTS
# =========================================================

def emissions_chart(df):
    fig = px.line(df, x="ano", y="emissoes_co2_mton", markers=True)
    return apply_layout(fig, "Carbon Emission Decarbonization Path", "Year", "Million Tons CO2")

def incidents_chart(df):
    fig = px.bar(df, x="ano", y="acidentes")
    return apply_layout(fig, "Operational Safety Record", "Year", "Total Incidents")

def environmental_investment_chart(df):
    fig = px.area(df, x="ano", y="investimento_ambiental_milhoes")
    return apply_layout(fig, "Sustainability Capital Expenditure", "Year", "Million R$")

# =========================================================
# MARKET CHARTS
# =========================================================

def stock_price_chart(df):
    fig = px.line(df, x="ano", y="preco_medio", markers=True)
    return apply_layout(fig, "PETR4 Market Valuation", "Year", "Price (R$)")

def trading_volume_chart(df):
    fig = px.bar(df, x="ano", y="volume_medio_milhoes")
    return apply_layout(fig, "Market Liquidity Analysis", "Year", "Million Shares")

def dividend_yield_chart(df):
    fig = px.area(df, x="ano", y="dividend_yield")
    return apply_layout(fig, "Dividend Yield History", "Year", "Yield (%)")
    return fig


def gas_production_chart(df):

    fig = px.bar(
        df,
        x="regiao",
        y="gas_milhoes_m3",
        color="regiao",
        title="Natural Gas Production"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Region",
        yaxis_title="Million m³"
    )

    return fig


def regional_share_chart(df):

    regional = (
        df.groupby("regiao")["petroleo_barris_dia"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        regional,
        names="regiao",
        values="petroleo_barris_dia",
        title="Production Share by Region"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


# =========================================================
# ESG CHARTS
# =========================================================

def emissions_chart(df):

    fig = px.line(
        df,
        x="ano",
        y="emissoes_co2_mton",
        markers=True,
        title="CO₂ Emissions Over Time"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Million Tons"
    )

    return fig


def incidents_chart(df):

    fig = px.bar(
        df,
        x="ano",
        y="acidentes",
        title="Operational Incidents"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Incidents"
    )

    return fig


def environmental_investment_chart(df):

    fig = px.area(
        df,
        x="ano",
        y="investimento_ambiental_milhoes",
        title="Environmental Investments"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Million R$"
    )

    return fig


# =========================================================
# MARKET CHARTS
# =========================================================

def stock_price_chart(df):

    fig = px.line(
        df,
        x="ano",
        y="preco_medio",
        markers=True,
        title="PETR4 Average Price"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Price (R$)"
    )

    return fig


def trading_volume_chart(df):

    fig = px.bar(
        df,
        x="ano",
        y="volume_medio_milhoes",
        title="Trading Volume"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Million Shares"
    )

    return fig


def dividend_yield_chart(df):

    fig = px.area(
        df,
        x="ano",
        y="dividend_yield",
        title="Dividend Yield Evolution"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="%"
    )

    return fig