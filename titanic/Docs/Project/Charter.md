# Project Charter

## Entendimento de negócio

O naufrágio do RMS Titanic é um dos naufrágios mais famosos da história. Em 15 de abril de 1912, durante sua viagem inaugural, o Titanic afundou após colidir com um iceberg, matando 1502 de 2224 passageiros e tripulantes com uma taxa de sobrevivência de aproximadamente 32%. Essa tragédia sensacional chocou a comunidade internacional e levou a melhores regulamentações de segurança para os navios.

Uma das razões pelas quais o naufrágio levou a tal perda de vidas foi que não havia botes salva-vidas suficientes para os passageiros e a tripulação. Embora houvesse algum elemento de sorte envolvido na sobrevivência do naufrágio, alguns grupos de pessoas eram mais propensos a sobreviver do que outros, como mulheres, crianças e a classe alta.


## Escopo

Para esse projeto, é preciso fazer uma análise e prever se um passageiro sobreviveu ao naufrágio do Titanic ou não.
Para cada um no conjunto de testes, você precisa informar um número para o IdPassageiro e o modelo deve prever um valor 0 ou 1 para a variável Sobreviveu, sendo 0 - Não e 1 - Sim. 

Com isso, teremos um problema de Classificação, para determinar quem sobreviveu ou não ao naufrágio:


* **Problema**: classificação binária
* **Algoritmo**: treinamento supervisionado
* **Base de dados**: arquivos csv originarios do Kaggle's Titanic: Machine Learning from Disaster (https://www.kaggle.com/c/titanic/data)
* **Variável alvo**: Sobreviveu (Survived)

## Métricas
* Objetivo qualitativo: Prever se um passageiro sobreviveu ou não ao naufrágio.
* Figura de mérito: Porcentagem de passageiros que você prevê corretamente. (Accuracy)
* Benchmarking: melhor que 80%.
* Métrica deve ser medida sobre um conjunto de teste de 30% dos dados.


## Planejamento
* Sprint 1: entendimento de negócio e preparação dos dados.
* Sprint 2: Análise de dados e construção de features.
* Sprint 3: Modelagem dos classificadores e avaliação dos resultados
* Sprint 4: Relatório dos resultados do modelo

## Arquitetura

* Dados:
  * Os dados são entregues através de 2 arquivos CSV
  * Relatório de dados disponível [aqui](../DataReport/Report.md "Relatório de dados")

* Modelos:
  * Classificador binário para estimar a probabilidade da pessoa ter sobrvivido ou não ao desastre.
  * Será utilizado um modelo linear de Regressão Logística.
  * Serão utilizados dois modelos de Bagging/Boosting: Adaboost e Gradboost.
  * Os hiper-parâmetros dos modelos serão ajustados segundo uma busca exaustiva em grid-search.
  * A base de dados será dividida em treino (70%) e teste (30%), mantendo a proporção de classes nos dois conjuntos de dados.
  * Os modelos serão avaliados considerando o conjunto de teste.
  * Os modelos e as análises sobre os dados podem ser estudadas [aqui](../Model/Report.md "Relatório de modelagem")
  
  
* Entregáveis:
  * Base de dados de teste com a previsão da sobrevivência de cada passageiro, em arquivo Excel.


## Comunicação
* Pontos de contato:
  * Consultoria: Paulo Pestana
