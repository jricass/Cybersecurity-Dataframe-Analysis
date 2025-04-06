import streamlit as st
import pandas as pd
import plotly.express as px
import base64 # Somente utilizado para conseguir usar uma imagem HTML

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

# ======================== Codigo do streamlit em si ======================== #

# TITULO
st.title('🌐 CyberSecurity Threats (2015 - 2024)')
st.markdown('---')

# Divisão - Links e Data Frame
c1, c2 = st.columns([1.5,4])

# Coluna 1 - Links de Acesso
# Link de Acesso do Data Frame
c1.markdown('### Sobre o Data Frame')
c1.markdown('O Data Frame utilizado consiste em registros de ameaças cibernéticas globais ocorridas entre os anos de 2015 e 2024. O Data Frame é proveniente do Kaggle e você pode acessa-lo por [aqui](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024).')

# Link de Acesso do Repositório
c1.markdown('### Acesse o Repositório do Projeto')
# Imagem do GitHub
c1.markdown(
    f"""
    <style>
        .img-github {{
            width: auto;
            max-height: 201px;
            border-radius: 8px;
        }}
    </style>
    <a href="https://github.com/jricass/Cybersecurity-Dataframe-Analysis"><img src="data:image/png;base64,{img_base64}" class="img-github"/><a>
    """,
    unsafe_allow_html=True
)

# Coluna 2 - Data Frame Info
c2.markdown('# Data Frame info')
c2.dataframe(table)
st.markdown('---')

# SideBar
st.sidebar.title("📓 Filtros")

selecao_years = st.sidebar.multiselect("📆 Ano", options=sorted(df["Year"].unique()), default=df["Year"].unique())

selecao_countries = st.sidebar.multiselect("🚩 País", options=sorted(df["Country"].unique()), default=df["Country"].unique())

selecao_attack_type = st.sidebar.multiselect("🦠 Tipo de Ataque", options=sorted(df["Attack Type"].unique()), default=df["Attack Type"].unique())

# isin Vai retornar True se o valor existe na lista
filtro = df[df["Year"].isin(selecao_years) & df["Country"].isin(selecao_countries) & df["Attack Type"].isin(selecao_attack_type)]

# Main - Métricas
st.markdown("# 📈 Métricas Gerais")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Incidentes", len(filtro))
col2.metric("Perda Total (Mi $)", f"{filtro['Financial Loss (in Million $)'].sum():,.2f}")
col3.metric("Usuários Afetados", f"{filtro['Number of Affected Users'].sum():,.0f}")
st.markdown('---')

# Main
tabs = st.tabs([
  "🕒 Incidentes por Ano",
  "💸 Perda por País",
  "📊 Setores Visados",
  "🕒 Tempo Médio de Resolução"
])

# Gráfico 1: Incidentes por Ano
with tabs[0]:
  st.subheader("🕒 Incidentes por Ano")
  ataqeu_por_ano = filtro.groupby("Year").size().reset_index(name="Total Ataques")
  fig1 = px.line(ataqeu_por_ano, x="Year", y="Total Ataques", markers=True)
  st.plotly_chart(fig1)

# Gráfico 2: Perda Financeira por País
with tabs[1]:
  st.subheader("💸 Perda Financeira por País")
  debito_por_pais = filtro.groupby("Country")["Financial Loss (in Million $)"].sum().reset_index()
  fig2 = px.bar(debito_por_pais.sort_values("Financial Loss (in Million $)", ascending=False), 
                x="Country", y="Financial Loss (in Million $)", color="Country")
  st.plotly_chart(fig2)

# Gráfico 3: Setores Visados
with tabs[2]:
  st.subheader("📊 Setores Mais Alvejados")
  setores_atingidos = filtro["Target Industry"].value_counts().reset_index()
  setores_atingidos.columns = ["Setor", "Número de Ataques"]
  fig3 = px.bar(setores_atingidos, x="Número de Ataques", y="Setor", orientation="h", color="Setor")
  st.plotly_chart(fig3)

# Gráfico 4: Tempo Médio de Resolução por Ano
with tabs[3]:
  st.subheader("🕒 Tempo Médio de Resolução de Incidentes")
  tempo_resolucao = filtro.groupby("Year")["Incident Resolution Time (in Hours)"].mean().reset_index()
  fig4 = px.line(tempo_resolucao, x="Year", y="Incident Resolution Time (in Hours)", markers=True)
  st.plotly_chart(fig4)

# Tipos e Fontes de Ataque
st.markdown('---')
graph1, graph2 = st.columns([1,1])

# Tipos de Ataque
graph1.markdown("## 🦠 Tipos de Ataque Mais Frequentes")
tipos_de_ataque = filtro["Attack Type"].value_counts().reset_index()
tipos_de_ataque.columns = ["Tipo de Ataque", "Quantidade"]
tipos = px.pie(tipos_de_ataque, values="Quantidade", names="Tipo de Ataque")
graph1.plotly_chart(tipos)

# Fontes de Ataque
graph2.markdown("## 🤖 Fontes de Ataque Mais Frequentes")
fontes_de_ataque = filtro["Attack Source"].value_counts().reset_index()
fontes_de_ataque.columns = ["Fonte", "Frequência"]
fontes = px.pie(fontes_de_ataque, values="Frequência", names="Fonte", hole=0.5)
graph2.plotly_chart(fontes)

st.markdown('---')
