# Relatório de Modelagem

Documento para registrar as análises e a modelagem desenvolvida.


## Análise de Dados

Foi feito o tratamento das colunas com valores nulos  e criação de novas variáveis fechando nas variáveis para o modelo:

classifier_variables = ['dropoff_latitude', 'dropoff_longitude',
       'passenger_count', 'pickup_latitude', 'pickup_longitude', 'hour_of_day',
       'day_of_week', 'day_of_year', 'year', 'eucl_distance', 'manh_distance']
	   
target = ['fare_amount']

A variável alvo é utilizada na análise da base de dados e na construção de novas features para o modelo.

	   
## Engineering features

Achamos que os dois fatores que mais importam na tarifa do táxi é a duração da corrida e a distância

### Duração

A duração da viagem não é dada e não podemos calcular porque a hora de chegada não é dada. Isso faz sentido porque a intenção do modelo é prever a tarifa **antes** da viagem acontecer

Algo que influencia a duração da viagem é a condição do tráfego. Podemos deduzir usando `pickup_datetime`.

* *hora do dia*: tráfego será menor durante a noite
* *dia da semana*: tráfego será menor nos finais de semana
* *dia do ano*: referiados e férias, por exemplo
* *ano*: pode ser influenciado por mudanças nas regras de transporte ou inflação

As variávéis eucl_distance e manh_distancia foram criada a partir das formulas:
 
Distância Euclideana: √((x1 – x2)² + (y1 – y2)²).

Distância Manhattan: |x1 – x2| + |y1 – y2|.


A escolha do modelo ficou a cargo do GradientBoost que obteve um RMSE de 2.5, um nota boa para esse projeto.
Será incorporado uma variável idTaxi com junção de valores de latitude e ano e a criação da feature estimated_fare com o valor da previsão da tarifa para exportação dos resultados para visualzição via API Rest.
