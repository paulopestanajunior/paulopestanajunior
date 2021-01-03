![](/newyork/header.png)

# Previsão de tarifa de táxi de Nova Iorque

A idéia de projeto veio a partir da competição do Kaggle: https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/overview. Abaixo a descrição:
A tarefa desse projeto é a de prever o valor da tarifa (inclusive pedágios) para uma corrida de táxi em Nova Iorque, dado os locais de partida e destino. **Embora você possa obter uma estimativa básica baseada apenas na distância entre os dois pontos, isso resultará em um RMSE de 5 a 8**, dependendo do modelo utilizado [...]. Seu desafio é ter resultados melhores do que esses usando técnicas de aprendizagem de máquina!

Apesar de oferecerem uma vasta base de dados no desafio, como precisava retirar dados via API, busquei o site original dos taxis de NY para realizar essa coleta, fazendo com que os dados dos taxis da companha Yellow Taxi fossem meus dados para modelagem e o da Green Taxi, os dados novos para previsão via API.

Os links utilizados foram:

# Yellow Taxi

urls = ["https://data.cityofnewyork.us/resource/t29m-gskq.json", #2018
        "https://data.cityofnewyork.us/resource/biws-g3hs.json", #2017
        "https://data.cityofnewyork.us/resource/uacg-pexx.json", #2016	
        "https://data.cityofnewyork.us/resource/2yzn-sicd.json", #2015	
        "https://data.cityofnewyork.us/resource/gkne-dk5s.json", #2014	
        "https://data.cityofnewyork.us/resource/t7ny-aygi.json", #2013	
        "https://data.cityofnewyork.us/resource/kerk-3eby.json", #2012	
        "https://data.cityofnewyork.us/resource/uwyp-dntv.json"  #2011
]

# Green Taxi
urls = ["https://data.cityofnewyork.us/resource/5gj9-2kzx.json", #2019
        "https://data.cityofnewyork.us/resource/w7fs-fd9i.json", #2018	
        "https://data.cityofnewyork.us/resource/5gj9-2kzx.json", #2017	
        "https://data.cityofnewyork.us/resource/hvrh-b6nb.json", #2016	
        "https://data.cityofnewyork.us/resource/gi8d-wdg5.json", #2015	
        "https://data.cityofnewyork.us/resource/2np7-5jsg.json", #2014
        "https://data.cityofnewyork.us/resource/ghpb-fpea.json", #2013
]

Após toda a parte de Coleta e Preparação dos dados, verifiquei a necessidade da criação de algumas features e algumas mudanças na base que originalmente teriam mais registros.
Ao final da modelagem, as features para realizar a previsão foram:

classifier_variables = ['dropoff_latitude', 'dropoff_longitude',
       'passenger_count', 'pickup_latitude', 'pickup_longitude', 'hour_of_day',
       'day_of_week', 'day_of_year', 'year', 'eucl_distance', 'manh_distance']
	   
Sendo minha variável alvo:

target_variable = 'fare_amount'

A variável alvo é utilizada na análise da base de dados e na construção de novas features para o modelo.

O GradientBoostingRegressor() foi o modelo escolhido ao final para deploy com um RMSE de ~2.5.
