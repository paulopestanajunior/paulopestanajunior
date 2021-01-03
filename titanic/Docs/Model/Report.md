# Relatório de Modelagem

Documento para registrar as análises e a modelagem desenvolvida.

Análise dos dados | [feature_analysis.ipynb](../../Code/Analysis/feature_analysis.ipynb) 

Modelagem dos Dados | [data_model.ipynb](../../Code/Model/modeling.ipynb) 

## Análise de Dados

Os dados foram processados e as colunas traduzidas para melhor entendimento do processo. 
Foi feito o tratamento das colunas com valores nulos ,tais quais:

* A coluna Cabine foi removida por conter mais de mil valores nulos e não ter muita relevância para predição de sobrevivência
* O valor faltante da coluna PortoEmbarque foi preenchido com a Moda.
* Os valores faltantes das colunas Tarifa e Idade foram preenchidos com suas respectivas médias.

Observando a descrição das variáveis númericas podemos concluir que:

* Pelo menos 75% dos passageiros não viajaram com os ***PaisFilhos***
* Pelo menos 50% dos passageiros não viajaram com os ***IrmaosCasal***
* A ***Idade*** da pessoa mais velha no barco é muito distante dos 75% restantes.
* O valor da ***Tarifa*** mais alta difere muito dos 75% restantes.
* ***Sobreviveu*** é uma variável categórica com valores de 0 e 1.

Observando a descrição das variáveis categóricas podemos concluir que:

* A coluna ***Nome*** possui apenas um registro repetido.
* A coluna ***Sexo*** possui dois valores possíveis sendo *Homem* o que mais frequente.
* A coluna ***Bilhete*** tem uma taxa alta de ocorrências duplicadas.
* A coluna ***Cabine*** possui muitos valores faltantes.
* ***PortoEmbarque*** possui três valores possíveis sendo *S* o que mais frequente.


Foi possível concluir também que:
* As mulheres e crianças tem mais propensão a sobreviver que os homens.
* Quanto maior a classe, maior a chance de sobrevivência, pois a maioria dos mortos na tragédia eram da Terceira Classe


Com base nas análises, foram criadas algumas features para predição do modelo ficar mais coesa, tais como:

|    **Variável**    	|                          **Definição**                          	|             **Chave**             	|
|:------------------:	|:---------------------------------------------------------------:	|:---------------------------------:	|
| Titulo             	| Pronome de tratamento retirado da variável Nome                 	|  Adulto, Casada, Menino, Solteira 	|
| TamanhoGrupo       	| Numéro de pessoas que possuem o mesmo sobrenome                 	|                                   	|
| SobrevivenciaGrupo 	| Quantidade de Mulheres e Crianças que possuem o mesmo sobrenome 	|                                   	|
| ExpectativaDeVida  	| Expectativa de sobrevivência                                    	|  0 = Mulheres/Crianças, 1 = Homem 	|

## Próximos passos

Após a análise preliminar, devemos seguir com o treinamento dos modelos de classificação, utilizando validação cruzada como forma de estimar os hiper-parâmetros do modelo e verificar qual tem melhor acurácia.

Foi usado um pipeline de modelos onde os três com maior score foram o GradientBoosting, AdaBoosting e Regressão Logística, sendo o primeiro o escolhido para submissão do nosso modelo final.
