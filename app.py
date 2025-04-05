import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Funções
# Função para Conversão de Imagem
def get_base64_image(image_path):
  with open(image_path, "rb") as img_file:
      return base64.b64encode(img_file.read()).decode()
# Converte a imagem
img_base64 = get_base64_image("assets/github.png")

# Definições Básicas
df = pd.read_csv('assets/Cybersecurity_Threats_2015-2024.csv')
table = pd.DataFrame({
  'Nome da Coluna': ['Country', 'Year', 'Attack Type', 'Target Industry', 'Financial Loss (in Million $)', 'Number of Affected Users', 'Attack Source', 'Security Vulnerability Type', 'Defense Mechanism Used', 'Incident Resolution Time (in Hours)'],

  'Descrição': ['País onde ocorreu o ataque', 'Ano do incidente', 'Tipo de ameaça (ex.: Malware, DDoS)', 'Setor alvo (ex.: Financeiro, Saúde)', 'Perda financeira estima (em Milhões de dólares)', 'Número de usuários comprometidos', 'Fonte de ataque (Hacker Group, Unknown)', 'Tipo de vulnerabilidade de sistema', 'Tipo de mecanismo de defesa utilizado como contramedida', 'Tempo de resolução do problema (em Horas)']
})
st.set_page_config(layout='wide')

# Header
st.title('🌐 CyberSecurity Threats (2015 - 2024)')
st.markdown('---')

# Divisão - Links e Data Frame
c1, c2 = st.columns([1.5,4])

# Coluna 1 - Links de Acesso
# Link de Acesso do Data Frame
c1.markdown('### Sobre o Data Frame')
c1.markdown('O Data Frame utilizado consiste em registros de ameaças cibernéticas globais ocorridas entre os anos de 2015 e 2024. O Data Frame é proveniente doKaggle e você pode acessa-lo por [aqui](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024).')

# Link de Acesso do Repositório
c1.markdown('### Acesse o Repositório do Projeto')
# Imagem do GitHub
c1.markdown(
    f"""
    <style>
        .img-github {{
            width: auto;
            max-height: 320px;
            border-radius: 8px;
        }}
    </style>
    <a href="https://github.com/jricass/Cybersecurity-Dataframe-Analysis"><img src="data:image/png;base64,{img_base64}" class="img-github"/><a>
    """,
    unsafe_allow_html=True
)

# Coluna 2 - Data Frame Info
c2.markdown('# Data Frame info:')
c2.dataframe(table)
st.markdown('---')

# SideBar
st.sidebar.title("📓 Filtros")

selecao_years = st.sidebar.multiselect("📆 Ano", options=sorted(df["Year"].unique()), default=df["Year"].unique())

selecao_countries = st.sidebar.multiselect("🚩 País", options=sorted(df["Country"].unique()), default=df["Country"].unique())

selecao_attack_type = st.sidebar.multiselect("🦠 Tipo de Ataque", options=sorted(df["Attack Type"].unique()), default=df["Attack Type"].unique())

filtro = df[df["Year"].isin(selecao_years) & df["Country"].isin(selecao_countries) & df["Attack Type"].isin(selecao_attack_type)]

# Main
st.markdown("# 📈 Métricas Gerais")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Incidentes", len(filtro))
col2.metric("Perda Total (Mi $)", f"{filtro['Financial Loss (in Million $)'].sum():,.2f}")
col3.metric("Usuários Afetados", f"{filtro['Number of Affected Users'].sum():,.0f}")
st.markdown('---')




