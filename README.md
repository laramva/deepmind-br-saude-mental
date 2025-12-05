# Mental Health Inequality: The Global Anxiety Treatment Gap (2000–2017)

Este projeto investiga a desigualdade global no acesso ao tratamento de ansiedade entre 2000 e 2017. Utilizando dados públicos sobre transtornos de ansiedade, foi desenvolvido um pipeline completo de análise, incluindo exploração, tratamento dos dados, construção de métricas e criação de um dashboard final em Power BI.

## Objetivos do Projeto

- Identificar o número de pessoas sem tratamento para ansiedade.
- Calcular o percentual global de indivíduos não tratados.
- Estimar o volume de pessoas que recebem algum nível de tratamento.
- Analisar a evolução temporal do tratamento insuficiente.
- Construir um dashboard claro e objetivo para comunicar os resultados.

## Fonte de Dados

Os dados utilizados são provenientes do conjunto:
Global Burden of Disease – Anxiety Disorders Treatment Gap

Arquivos utilizados:
- data/raw/anxiety-disorders-treatment-gap.csv  
- data/processed/anxiety_treatment_gap_long.csv  

O dataset contém:
- Total de pessoas com transtornos de ansiedade
- Número de pessoas sem tratamento
- Número de pessoas com tratamento parcial
- Percentuais de não tratamento ao longo dos anos

## Estrutura do Projeto

project/  
 ├── data/  
 │   ├── raw/                      # dados brutos  
 │   ├── processed/                # dados tratados  
 ├── notebooks/  
 │   ├── 01_coleta_exploracao.ipynb  
 │   ├── 02_tratamento_feature_engineering.ipynb  
 ├── src/  
 │   ├── data_processing.py        # funções ETL  
 │   ├── modeling.py               # reservado para análises futuras  
 ├── docs/  
 │   ├── Mental_Health_Anxiety_Treatment_Gap.pbix  # dashboard Power BI  
 │   ├── fontes_de_dados.md  
 ├── reports/  
 │   ├── placeholder.txt  
 ├── README.md  

## Visão Geral do Dashboard

O dashboard final (disponível em docs/Mental_Health_Anxiety_Treatment_Gap.pbix) apresenta:

- 19,5 milhões de pessoas com ansiedade sem tratamento adequado.
- Cerca de 75% da população com transtornos de ansiedade permanece sem tratamento.
- Aproximadamente 25% recebem algum nível de tratamento.
- A taxa de não tratamento nunca ficou abaixo de 70% entre 2000 e 2017.

Elementos visuais principais:
- Indicadores numéricos (KPIs)
- Distribuição global dos tipos de tratamento
- Evolução temporal da taxa de não tratamento
- Comparação entre tratamento total, parcial e ausência de tratamento

## Tecnologias Utilizadas

- Python 3.10  
- Pandas  
- Numpy  
- Jupyter Notebook  
- Power BI Desktop  
- Visual Studio Code  

## Como Reproduzir o Projeto

1. Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git  
cd seu-repositorio  

2. Instale as dependências:

pip install -r requirements.txt  

3. Abra os notebooks:

jupyter notebook notebooks/  

4. Abra o dashboard no Power BI:

docs/Mental_Health_Anxiety_Treatment_Gap.pbix  

## Insights Principais

- A maioria das pessoas com transtornos de ansiedade não recebe nenhum tratamento.
- O volume estimado de indivíduos sem tratamento ultrapassa 19 milhões.
- A taxa global média de não tratamento gira em torno de 75%.
- Há flutuações temporais, porém a taxa nunca caiu abaixo de 70%.
- O tratamento parcial é mais comum do que o tratamento completo.

## Roadmap

- Publicar o dashboard no Power BI Service.
- Criar relatório técnico completo na pasta reports/.
- Desenvolver narrativa analítica adicional para portfólio.
- Implementar testes automatizados no pipeline de dados.

## Licença

Este projeto está licenciado sob a licença MIT.

## Autora

Lara Maciel  
Profissional multidisciplinar com experiência em ensino, SDR e análise de dados, com foco em visualização, storytelling analítico e projetos aplicados à saúde mental.

Eu, **Lara Maciel Vargas Alves**, portador(a) da Cédula de Identidade RG n° **6007109**, inscrito no CPF sob o n° **034.870.971-41**, autorizo a cessão do meu projeto em favor da Semantix, bem como a divulgação do meu nome como autor responsável pelo projeto, uma vez que será possível incluir esse trabalho em meu portfólio de trabalho.

Nesse sentido, autorizo também a divulgação dos meus contatos telefone e e-mail para a Semantix, tão somente para uso interno com finalidade única de contato em decorrência da elaboração do projeto mencionado.
