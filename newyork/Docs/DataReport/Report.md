
# Relatório de Dados

Esse relatório das bases de dados do projeto.


## Bases de dados

A base de dados utilizada foi uma api de dados advindas do site: https://data.cityofnewyork.us/browse?Dataset-Information_Agency=Taxi+and+Limousine+Commission+%28TLC%29&


Processado para qualidade de dados | [data_prep_yellow.ipynb](../../Code/DataPrep/data_prep_yellow.ipynb) | 


* Base Taxi

classifier_variables = ['dropoff_latitude', 'dropoff_longitude',
       'passenger_count', 'pickup_latitude', 'pickup_longitude', 'hour_of_day',
       'day_of_week', 'day_of_year', 'year', 'eucl_distance', 'manh_distance']
	   
target = ['fare_amount']

A variável alvo é utilizada na análise da base de dados e na construção de novas features para o modelo.



|    **Variável**   |           **Definição**           |                     **Chave**                    |
|:-----------------:|:---------------------------------:|:------------------------------------------------:|
| dropoff_latitude  | Latitude de chegada da corrida    |                                                  |
| dropoff_longitude | Longitude de chegada da corrida   | 					                               |
| passenger_count   | Número de passageiros da corrida  | 											       |
| pickup_latitude   | Latitude de partida da corrida    |                                                  |
| pickup_longitude  | Latitude de partida da corrida    | 					                               |
| hour_of_day       | Horário do dia da corrida         | 0 à 23                                           |
| day_of_week       | Dia da semana da corrida   		| 0-Dom, 1-Seg, 2-Ter, 4-Qua, 5-Qui, 6-Sex, 7-Sáb  |
| day_of_year       | Dia do ano da corrida      		| 0 a 365                                          |
| year		        | Ano da corrida      				|                                                  |
| eucl_distance     | Distância Euclidiana              |                                                  |
| manh_distance     | Distância Manhathan	            |                                                  |

		

## Parâmetros Numéricos
* ### Contínuas
    - dropoff_latitude
    - dropoff_longitude
    - pickup_latitude
    - pickup_longitude
    - eucl_distance
    - manh_distance
    
* ### Discretas
	- passenger_count
    - hour_of_day
    - day_of_week
	- day_of_year
	- year
    

