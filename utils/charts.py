import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# FINANCIAL CHARTS
# =========================================================

def revenue_chart(df):

    fig = px.line(
        df,
        x="ano",
        y="receita_bilhoes",
        markers=True,
        title="Revenue Over Time"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Revenue (Billion R$)"
    )

    return fig


def profit_vs_ebitda_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df["ano"],
            y=df["lucro_bilhoes"],
            name="Net Profit"
        )
    )

    fig.add_trace(
        go.Bar(
            x=df["ano"],
            y=df["ebitda_bilhoes"],
            name="EBITDA"
        )
    )

    fig.update_layout(
        title="Profit vs EBITDA",
        barmode="group",
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Billion R$"
    )

    return fig


def dividends_chart(df):

    fig = px.area(
        df,
        x="ano",
        y="dividendos_bilhoes",
        title="Dividends Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Dividends (Billion R$)"
    )

    return fig


def revenue_growth_chart(df):

    crescimento = (
        df["receita_bilhoes"].pct_change()
    ) * 100

    df_growth = df.copy()

    df_growth["crescimento"] = crescimento

    fig = px.scatter(
        df_growth,
        x="ano",
        y="crescimento",
        size="crescimento",
        title="Revenue Growth Percentage"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Growth (%)"
    )

    return fig


# =========================================================
# PRODUCTION CHARTS
# =========================================================

def oil_production_chart(df):

    fig = px.line(
        df,
        x="ano",
        y="petroleo_barris_dia",
        color="regiao",
        markers=True,
        title="Oil Production by Region"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Year",
        yaxis_title="Barrels per Day"
    )

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