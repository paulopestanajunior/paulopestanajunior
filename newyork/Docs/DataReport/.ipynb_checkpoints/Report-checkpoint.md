
# Relatório de Dados

Esse relatório das bases de dados do projeto.


## Bases de dados

A base de dados utilizada são 2 arquivos csv's originários do Kaggle's Titanic: Machine Learning from Disaster (https://www.kaggle.com/c/titanic/data)


Processado para qualidade de dados | [data_prep.ipynb](../../Code/DataPrep/data_prep.ipynb) | 


* Base Titanic

Colunas originais:   ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']. 
Colunas traduzidas:  ['IdPassageiro, Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', IrmaosCasal','PaisFilhos', 'Bilhete', 'Tarifa', 'Cabine', 'PortoEmbarque']
, onde:



|  **Variável** |            **Definição**            |                     **Chave**                    |
|:-------------:|:-----------------------------------:|:------------------------------------------------:|
| IdPassageiro  | ID do passageiro do navio           |                                                  |
| Sobreviveu    | Sobreviveu ou não ao desastre       | 0 = Não, 1 = Sim                                 |
| Classe        | Tipo de classe de passagem          | 1 = Primeira, 2 =   Segunda, 3 = Terceira        |
| Nome          | Nome do Passageiro                  |                                                  |
| Sexo          | Gênero do passageiro                | male \| female                                   |
| Idade         | Idade do passageiro                 |                                                  |
| IrmaosCasal   | Número de irmãos / cônjuges a bordo |                                                  |
| PaisFilhos    | Número de pais / filhos a bordo     |                                                  |
| Bilhete       | Número do Bilhete                   |                                                  |
| Tarifa        | Valor da passagem pago              |                                                  |
| Cabine        | Código de identificação da Cabine   |                                                  |
| PortoEmbarque | Porto de origem do embarque         | C = Cherbourg, Q =   Queenstown, S = Southampton |
		
Observações das variáveis:		
		
Classe: Classificação por status socioeconômico		
Primeira = Alta		
Segunda = Média		
Terceira = Baixa		
		
Idade: a idade é fracionária se for menor que 1. Se a idade for estimada, é na forma de xx.5		
		
IrmaosCasal: O conjunto de dados define as relações familiares dessa maneira:		
Irmaos = irmão, irmã, meio-irmão, meia-irmã		
Casal = marido, esposa (amantes e noivos foram ignorados)		
		
PaisFilhos: O conjunto de dados define as relações familiares da seguinte forma:		

Pais = mãe, pai
Filhos = filha, filho, enteada, enteado
Algumas crianças viajavam apenas com uma babá, portanto PaisFilhos = 0 para elas.

## Parâmetros Categóricos 
* ### Nominais
    - Sexo
    - PortoEmbarque
    - Sobreviveu
   
* ### Ordinais
    - Classe

## Parâmetros Numéricos
* ### Contínuas
    - Idade
    - Tarifa
    
* ### Discretas
    - PaisFilhos
    - IrmaosCasal
    
## Parâmetros Alfanuméricos
* Bilhete
* Nome
