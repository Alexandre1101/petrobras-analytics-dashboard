def financial_kpis(df):

    receita_atual = df["receita_bilhoes"].iloc[-1]
    receita_anterior = df["receita_bilhoes"].iloc[-2]

    lucro_atual = df["lucro_bilhoes"].iloc[-1]
    lucro_anterior = df["lucro_bilhoes"].iloc[-2]

    ebitda_atual = df["ebitda_bilhoes"].iloc[-1]
    ebitda_anterior = df["ebitda_bilhoes"].iloc[-2]

    receita_delta = (
        (receita_atual - receita_anterior)
        / receita_anterior
    ) * 100

    lucro_delta = (
        (lucro_atual - lucro_anterior)
        / lucro_anterior
    ) * 100

    ebitda_delta = (
        (ebitda_atual - ebitda_anterior)
        / ebitda_anterior
    ) * 100

    return (
        receita_atual,
        lucro_atual,
        ebitda_atual,
        receita_delta,
        lucro_delta,
        ebitda_delta
    )