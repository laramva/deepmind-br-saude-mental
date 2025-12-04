# DeepMind BR: Insights para Políticas Públicas em Saúde Mental

Projeto desenvolvido no contexto do Programa de Empregabilidade da EBAC em parceria com a Semantix.

## 1. Visão Geral

O objetivo deste projeto é utilizar análise de dados e técnicas simples de machine learning para identificar padrões de risco e desigualdade no acesso aos serviços de saúde mental no Brasil.

A partir de dados públicos, buscamos responder, por exemplo:
- Quais regiões apresentam maior risco de agravo de transtornos mentais?
- Onde o acesso a serviços especializados (como CAPS) é mais limitado?
- Como fatores socioeconômicos se relacionam com indicadores de saúde mental?

## 2. Problema

**Descrição do problema**

No Brasil, transtornos mentais são uma causa crescente de incapacidade, sofrimento e impacto econômico. Ao mesmo tempo, o acesso aos serviços de saúde mental é desigual entre regiões, faixas de renda e contextos urbanos/rurais.

Este projeto busca mapear:
- Áreas com maior demanda potencial por cuidado em saúde mental;
- Lacunas de acesso a serviços especializados;
- Relações entre indicadores socioeconômicos e desfechos em saúde mental.

## 3. Relevância

A saúde mental é um tema sensível e prioritário em políticas públicas. Com uma análise baseada em dados, é possível apoiar decisões como:
- Priorização de abertura de novos CAPS;
- Alocação de recursos humanos e financeiros;
- Estratégias de prevenção e campanhas específicas por região.

Este estudo não substitui decisões de gestores, mas fornece **insights** que podem orientar políticas mais eficientes e equitativas.

## 4. Metodologia (Resumo)

1. Coleta de dados públicos (ex.: DataSUS, IBGE, etc.).
2. Limpeza e padronização das bases (tratamento de nulos, padronização de nomes de municípios, etc.).
3. Análise exploratória de dados (EDA) para entender padrões e outliers.
4. Criação de indicadores (ex.: internações por 100 mil habitantes, número de CAPS por 100 mil habitantes).
5. Aplicação de técnicas simples de machine learning (ex.: clusterização ou regressão) para identificar perfis de risco.
6. Geração de visualizações e painéis com foco em comunicação clara para tomadores de decisão.

Detalhes da implementação podem ser vistos na pasta `notebooks/` e em `src/`.

## 5. Estrutura do Repositório

- `data/raw/` – dados brutos, diretamente extraídos de fontes públicas.
- `data/processed/` – dados tratados e prontos para modelagem/visualização.
- `notebooks/` – notebooks Jupyter com etapas do projeto (EDA, tratamento, modelagem).
- `src/` – scripts Python auxiliares (tratamento de dados, visualizações, modelos).
- `reports/` – relatórios e gráficos finais.
- `docs/` – materiais de apoio, diagramas e apresentações.

## 6. Declaração de Autorização LGPD

Eu, [NOME COMPLETO], portador(a) da Cédula de Identidade RG n° [RG], inscrito no CPF sob o n° [CPF], autorizo a cessão do meu projeto em favor da Semantix, bem como a divulgação do meu nome como autor responsável pelo projeto, uma vez que será possível incluir esse trabalho em meu portfólio de trabalho.

Nesse sentido, autorizo também a divulgação dos meus contatos telefone e e-mail para a Semantix, tão somente para uso interno com finalidade única de contato em decorrência da elaboração do projeto mencionado.

## 7. Tecnologias Utilizadas

- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib / Plotly
- Scikit-learn (para modelos simples)

## 8. Status do Projeto

🚧 Em desenvolvimento: estrutura inicial do repositório e planejamento de coleta de dados.
