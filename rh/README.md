![](/rh/header.png)

# Project Charter

## Entendimento de negócio

Contratar e reter funcionários são tarefas extremamente complexas que exigem capital, tempo e habilidades. Pequenos empresários gastam em torno de 40% das horas de trabalho em tarefas que não geram receitas, como a contratação.
O departamento de RH da empresa coletou dados dos funcionários e gostaria que de quais são mais propensos para sair do emprego e alguns exemplos de dados:

- Envolvimento com o trabalho
- Escolaridade
- Satisfação com o trabalho
- Métricas de desempenho
- Relacionamento
- Equilíbrio entre atividades pessoais e profissionais

## Escopo

Para esse projeto, é preciso utilizar uma base de dados histórica para prever se um funcionário está propenso a sair ou não da empresa
Com isso, teremos um problema de Classificação, para determinar se o funcionário vai sair ou não:


* **Problema**: classificação binária
* **Algoritmo**: treinamento supervisionado
* **Base de dados**: arquivos csv originarios do Kaggle's [IBM HR Analytics Employee Attrition & Performance] (https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset) com classes desbalanceadas.
* **Variável alvo**: Attrition

## Métricas
* Objetivo qualitativo: Prever se um funcionário vai sair da empresa ou não
* Figura de mérito: Porcentagem de funcionários que você prevê corretamente. (Accuracy)
* Benchmarking: melhor que 80%.
* Métrica deve ser medida sobre um conjunto de teste de 25% dos dados.


## Planejamento
* Sprint 1: entendimento de negócio e preparação dos dados.
* Sprint 2: Análise de dados e construção de features.
* Sprint 3: Modelagem dos classificadores e avaliação dos resultados
* Sprint 4: Relatório dos resultados do modelo

## Arquitetura

* Dados:
  * Modelo para previsões futuras
  * Relatório de dados disponível [aqui](../DataReport/Report.md "Relatório de dados")

* Modelos:
  * Classificador binário para estimar a probabilidade do funcionário sair ou não da empresa.
  * Será utilizado um modelo linear de Regressão Logística.
  * Serão utilizados ainda dois modelos: Randon Forest e Redes Neurais..
  * A base de dados será dividida em treino (75%) e teste (25%), mantendo a proporção de classes nos dois conjuntos de dados.
  * Os modelos serão avaliados considerando o conjunto de teste.
  * Os modelos e as análises sobre os dados podem ser estudadas [aqui](../Model/Report.md "Relatório de modelagem")
  
  
* Entregáveis:
  * Modelo para futuras previsões
  
![](/rh/rh1.png)

![](/rh/rh2.png)

![](/rh/rh3.png)


## Comunicação
* Pontos de contato:
  * Data Scientist: Paulo Pestana
