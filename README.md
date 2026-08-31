# ⛽ Petrobras Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-blueviolet)
![Status](https://img.shields.io/badge/Status-Concluído-success)

Dashboard interativo desenvolvido com **Streamlit, Pandas e Plotly** para análise de dados financeiros, operacionais e de ESG fictícios inspirados no setor de energia brasileiro.

---

## 🚀 Demonstração

🌐 **Streamlit Cloud:**

https://petrobras-analytics-dashboard-e6fupnnaxjjt8axdbdk4sh.streamlit.app/

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido para simular um ambiente real de **Business Intelligence (BI)** e **análise de dados**, utilizando um conjunto de dados fictícios inspirado no setor de energia brasileiro.

O dashboard apresenta visualizações interativas e indicadores-chave de desempenho (**KPIs**) para diferentes áreas de análise:

* Desempenho financeiro
* Produção de petróleo e gás
* Indicadores de ESG
* Análise de mercado

O principal objetivo do projeto é demonstrar conhecimentos práticos em:

* Análise de dados
* Visualização de dados
* Desenvolvimento de dashboards
* Modularização de projetos Python
* Conceitos de Business Intelligence
* Fluxo de trabalho com Git e GitHub

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Streamlit**
* **Pandas**
* **Plotly**
* **OpenPyXL**

---

## 🚀 Funcionalidades

### 📊 Análise Financeira

* Análise de receita
* Acompanhamento do lucro líquido
* Indicadores de EBITDA
* Análise de dividendos

### 🛢️ Análise de Produção

* Acompanhamento da produção de petróleo
* Indicadores de produção de gás natural
* Comparação da produção por região

### 🌱 Dashboard de ESG

* Análise de emissões de CO₂
* Investimentos ambientais
* Acompanhamento de incidentes operacionais

### 📈 Dashboard Interativo

* Gráficos dinâmicos
* Cards com KPIs
* Navegação por menu lateral
* Layout adaptável

---

## 📂 Estrutura do projeto

```text
petrobras-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── petrobras_dados_ficticios.xlsx
│
├── pages/
│   ├── 1_financial_overview.py
│   ├── 2_production_analysis.py
│   ├── 3_esg_analysis.py
│   └── 4_market_analysis.py
│
├── utils/
│   ├── load_data.py
│   ├── charts.py
│   ├── kpis.py
│   └── formatting.py
│
├── assets/
│   ├── logo.png
│   ├── dashboard_preview.png
│   ├── dashboard_p1.png
│   ├── dashboard_p2.png
│   ├── dashboard_p3.png
│   └── dashboard_p4.png
│
└── .streamlit/
    └── config.toml
```

---

## 🖥️ Visualização do Dashboard

### Visão geral

![Prévia do Dashboard](assets/dashboard_preview.png)

---

### 📊 Dashboard Financeiro Executivo

![Análise Financeira](assets/dashboard_p1.png)

---

### 🛢️ Inteligência de Produção

![Análise de Produção](assets/dashboard_p2.png)

---

### 🌱 ESG e Sustentabilidade

![Indicadores de ESG](assets/dashboard_p3.png)

---

### 📈 Dashboard de Inteligência de Mercado

![Análise de Mercado](assets/dashboard_p4.png)

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Alexandre1101/petrobras-analytics-dashboard.git
```

### 2. Acesse a pasta do projeto

```bash
cd petrobras-analytics-dashboard
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run app.py
```

Após executar o comando, o Streamlit disponibilizará o dashboard localmente no navegador.

---

## 📊 Dataset

Este projeto utiliza um **conjunto de dados fictícios**, criado exclusivamente para fins educacionais e de portfólio.

Os dados apresentados **não representam informações financeiras, operacionais ou corporativas reais da Petrobras**.

---

## 🎯 Principais conhecimentos demonstrados

* Análise Exploratória de Dados (EDA)
* Desenvolvimento de dashboards
* Visualização de dados interativa
* Desenvolvimento de KPIs
* Processamento de dados com Pandas
* Organização e modularização de projetos Python
* Desenvolvimento de aplicações com Streamlit
* Git e GitHub
* Conceitos de Business Intelligence

---

## 🔮 Melhorias futuras

* Implementação de modelos de previsão com Machine Learning
* Análise das ações PETR4
* Integração com APIs em tempo real
* Sistema de filtros avançados
* Integração com banco de dados
* Containerização e deploy utilizando Docker

---

## 👨‍💻 Autor

Desenvolvido por **Alexandre Soares Neves Junior**

GitHub: [Alexandre1101](https://github.com/Alexandre1101)

---

## 📄 Licença

Este projeto foi desenvolvido exclusivamente para **fins educacionais e de portfólio**.
