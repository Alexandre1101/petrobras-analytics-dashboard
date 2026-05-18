import plotly.express as px

def revenue_chart(df):

    fig = px.line(
        df,
        x="ano",
        y="receita_bilhoes",
        markers=True,
        title="Receita ao Longo dos Anos"
    )

    return fig

def revenue_chart(df):

    fig = px.line(
        df,
        x="ano",
        y="receita_bilhoes",
        markers=True,
        title="Revenue Over Time"
    )

    return fig