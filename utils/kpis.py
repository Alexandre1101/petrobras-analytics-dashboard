def financial_kpis(df):

    # valores atuais
    receita_atual = df["receita_bilhoes"].iloc[-1]
    lucro_atual = df["lucro_bilhoes"].iloc[-1]
    ebitda_atual = df["ebitda_bilhoes"].iloc[-1]
    dividendos_atual = df["dividendos_bilhoes"].iloc[-1]

    # valores anteriores
    receita_anterior = df["receita_bilhoes"].iloc[-2]
    lucro_anterior = df["lucro_bilhoes"].iloc[-2]
    ebitda_anterior = df["ebitda_bilhoes"].iloc[-2]
    dividendos_anterior = df["dividendos_bilhoes"].iloc[-2]

    # cálculo das variações
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

    dividendos_delta = (
        (dividendos_atual - dividendos_anterior)
        / dividendos_anterior
    ) * 100

    return {
        "receita": receita_atual,
        "lucro": lucro_atual,
        "ebitda": ebitda_atual,
        "dividendos": dividendos_atual,

        "receita_delta": receita_delta,
        "lucro_delta": lucro_delta,
        "ebitda_delta": ebitda_delta,
        "dividendos_delta": dividendos_delta
    }