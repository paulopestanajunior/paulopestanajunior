# Project Charter

## Entendimento de negócio

A tarefa desse projeto é a de prever o valor da tarifa (inclusive pedágios) para uma corrida de táxi em Nova Iorque, dado os locais de partida e destino. **Embora você possa obter uma estimativa básica baseada apenas na distância entre os dois pontos, isso resultará em um RMSE de 5 a 8**, dependendo do modelo utilizado [...]. Seu desafio é ter resultados melhores do que esses usando técnicas de aprendizagem de máquina!


## Escopo

Para esse projeto, é preciso fazer uma análise e prever as tarifas das novas corridas de Taxi da cidade de Nova York

Com isso, teremos um problema de Regressão, para determinar o preço da tarifa:


* **Problema**: regressão
* **Algoritmo**: treinamento supervisionado
* **Base de dados**: api de dados advindas do site: https://data.cityofnewyork.us/browse?Dataset-Information_Agency=Taxi+and+Limousine+Commission+%28TLC%29&
* **Variável alvo**: fare_amount

## Métricas
* Objetivo qualitativo: Prever a tarifa da corrida.
* Figura de mérito: RMSE
* Métrica deve ser medida sobre dados novos.


## Planejamento
* Sprint 1: entendimento de negócio e preparação dos dados.
* Sprint 2: Análise de dados e construção de features.
* Sprint 3: Modelagem dos classificadores e avaliação dos resultados
* Sprint 4: Relatório dos resultados do modelo

## Arquitetura

* Dados:
  * Os dados são entregues via api rest Django com Dash
  * Relatório de dados disponível [aqui](../DataReport/Report.md "Relatório de dados")

* Modelos:
  * Regressor para estimar a tarifa das corridas de taxi na cidade de Nova York.
  * Será utilizado o modelo Gradboost.
  * A base de dados será dividida em treino (70%) e teste (30%), mantendo a proporção de classes nos dois conjuntos de dados.
  * Os modelos serão avaliados considerando o conjunto de teste.
  * Os modelos e as análises sobre os dados podem ser estudadas [aqui](../Model/Report.md "Relatório de modelagem")
  
  
* Entregáveis:
  * API Django com Dash.


## Comunicação
* Pontos de contato:
  * Consultoria: Paulo Pestana
