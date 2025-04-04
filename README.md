# Cybersecurity-Dataframe-Analysis

# Introdução

## Escolha do Data Frame
O Data Frame em questão consiste em registros de ameaças cibernéticas globais ocorridas entre os anos de 2015 e 2024. Você pode acessar o Data Frame utilizado por [aqui](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024).

## Justificativa da Decisão/Aplicabilidade

### 📂 Sobre o Data Frame
> O Data Frame está dividido da seguinte maneira:

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

### 🔍 Escolha do Data Frame
A escolha deste Data Frame foi baseada em sua **estrutura bem definida**, **variedade de atributos** e **potencial analítico** e **visualização de dados**.

A base cobre um período de 10 anos (2015 a 2024) e contém 10 colunas com informações críticas e variadas, como:
 
- **Dimensões categóricas** (país, tipo de ataque, setor-alvo, tipo de vulnerabilidade, mecanismo de defesa);>    
- **Variáveis numéricas contínuas** (perda financeira em milhões, número de usuários afetados, tempo de resolução);
- **Componente temporal** (ano dos ataques), que permite a análise de tendências. 

Esse equilíbrio entre atributos categóricos, temporais e numéricos oferece **excelentes oportunidades para aplicar técnicas de:**
 
 - Limpeza e padronização de dados;
 - Criação de novas métricas e colunas derivadas;
 - Análise de correlação entre variáveis;     
 - Identificação de padrões relevantes com visualizações interativas;
 - Segmentação e comparação entre diferentes grupos (por país, setor, tipo de ataque, etc.).

A base também se destaca por estar livre de dados ausentes e duplicações, permitindo concentrar esforços na **engenharia de atributos, padronização e análise de valor agregado**. Isso viabiliza a construção de dashboards informativos e funcionais com foco em **extração de insights estratégicos**, que é o principal objetivo deste projeto.

## 1.3 Entendimento Inicial do Data Frame.
### Verificações Básicas
- df.info()
- df.describe()
- df.insnull().sum()
- df.duplicated().sum()
### Tratamentos Iniciais

---
# 2 Análise Exploratória de Dados
## 2.1 Análises Exploratórias

## 2.2 Estatísticas Descritivas

## 2.3 Visualizações Básicas

## 2.4 Identificação de Tendências Preliminares na Análise

---
# 3 Tratamento de Dados
## 3.1 Identificação de Quaisquer Problemas
## 3.2 Aplicação de Tratamentos
#### Valores Ausentes
#### Correção de Erros
#### Remoção de Outliers

---
# 4 Planejamento do Dashboard
## 4.1 Visualizações que serão incluídas
## 4.2 Consideração do Público Alvo
## 4.3 Escolha das visualizações que transmitam efetivamente as informações relevantes

---
# 5 Criação do Dashboard
## 5.1 Plotly
## 5.2 Implementação de Filtros para exploração dinâmica dos dados.

---
