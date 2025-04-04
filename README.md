# Cybersecurity-Dataframe-Analysis

# 🚀 Sobre o Projeto
O objetivo deste projeto é permitir a aplicação dos conhecimentos de análise de dados estatísticos provenientes de um determinado **Data Frame**, utilizando a biblioteca **Pandas** para a análise de dados e o **Streamlit** para a exibição de Dashboards interativos.

## 📂 Sobre o Data Frame
O Data Frame em questão consiste em registros de ameaças cibernéticas globais ocorridas entre os anos de 2015 e 2024. O Data Frame é proveniente do Kaggle e você pode acessa-lo por [aqui](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024).

O Data Frame está dividido da **seguinte maneira**:

| Nome da Coluna            | Descrição                                         |
| ------------------------- | ------------------------------------------------- |
| **Country**               | País onde ocorreu o ataque                        |
| **Year**                  | Ano do incidente                                  |
| **Threat Type**           | Tipo de ameaça cibernética (ex.: Malware, DDoS)   |
| **Attack Vector**         | Método do ataque (ex.: Phishing, SQL Injection)   |
| **Affected Industry**     | Setor alvo (ex.: Financeiro, Saúde)               |
| **Data Breached (GB)**    | Volume de dados comprometidos (em GB)             |
| **Financial Impact ($M)** | Perda financeira estimada (em milhões de dólares) |
| **Severity Level**        | Nível de severidade (Baixo, Médio, Alto, Crítico) |
| **Response Time (Hours)** | Tempo para mitigar o ataque (em horas)            |
| **Mitigation Strategy**   | Contramedidas adotadas                            |

## 🔍 Escolha do Data Frame
A escolha deste Data Frame foi baseada em sua **estrutura bem definida**, **variedade de atributos** e **potencial analítico** e **visualização de dados**.

Cobrindo um período de 10 anos (2015 a 2024) e contém 10 colunas com informações variadas.

Esse equilíbrio entre atributos categóricos, temporais e numéricos oferece **excelentes oportunidades para a aplicação das técnicas a seguir:**

 - Limpeza e padronização de dados;
 - Criação de novas métricas e colunas derivadas;
 - Análise de correlação entre variáveis;     
 - Identificação de padrões relevantes com visualizações interativas;
 - Segmentação e comparação entre diferentes grupos (por país, setor, tipo de ataque, etc.).

> O Data Frame também esta livre de dados ausentes e duplicações.

# Entendimento Inicial do Data Frame.
## Verificações Básicas
- df.info()
- df.describe()
- df.insnull().sum()
- df.duplicated().sum()
## Tratamentos Iniciais

---
# Análise Exploratória de Dados
## Análises Exploratórias
## Estatísticas Descritivas
## Visualizações Básicas
## Identificação de Tendências Preliminares na Análise

---
# Tratamento de Dados
## Identificação de Quaisquer Problemas
## Aplicação de Tratamentos
### Valores Ausentes
### Correção de Erros
### Remoção de Outliers

---
# Planejamento do Dashboard
## Visualizações que serão incluídas
## Consideração do Público Alvo
## Escolha das visualizações que transmitam efetivamente as informações relevantes

---
# Criação do Dashboard
## Plotly
## Implementação de Filtros para exploração dinâmica dos dados.

---
