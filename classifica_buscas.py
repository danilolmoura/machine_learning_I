#coding: utf-8


#1. Neste exercício, incluímos a biblioteca Pandas para abrir o arquivo CSV, extrair os dados e tratar variáveis categóricas(dummies).


#Neste bloco:
##1. Abrimos o arquivo csv através do pandas e recuperamos os dados
##2. Realizamos a conversão destes dados para Array, para que possam ser utilizados posteriormente
from collections import Counter
import pandas as pd 
df = pd.read_csv( 'csv/busca.csv' ) #df equivale a dataframe

X_df = df[['home', 'busca', 'logado']] #Quando queremos mais de 1 coluna, devendo passar um array contendo essas colunas
Y_df = df['comprou'] 


Xdummies_df = pd.get_dummies( X_df )
Ydummies_df = Y_df


X = Xdummies_df.values # .values devolve um array
Y = Ydummies_df.values # .values devolve um array


#Neste bloco definimos:
##1. A porcetangem de dados que serão utilizadas tanto para o treinamento treino quanto para teste
##2. Recuperamos os valores que serão utilizados tanto para o treinamento quanto para o teste
porcentagem_de_treino = 0.9
tamanho_de_treino = int( porcentagem_de_treino * len( Y ) ) #Define 90% do total para treino
tamanho_de_teste  = int( len( Y ) - tamanho_de_treino )#Define 10% do total para teste

treino_dados 	 = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados     = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]



#Neste bloco:
##1. Realizamos o treinamento do algoritmo
##2. Exibimos a resposta do algoritmo
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB( ) # cria o modelo
modelo.fit( treino_dados, treino_marcacoes ) # treina o modelo

resultado = modelo.predict( teste_dados ) #preveja
acertos = ( resultado == teste_marcacoes )

total_de_acertos = sum( acertos )
total_de_elementos = len( teste_dados )
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print( "Taxa de acerto base: %f" % taxa_de_acerto )
print( total_de_elementos )



#Neste bloco:
##1. A eficácia do algoritmo que chuta um único valor
acerto_base = max( Counter(teste_marcacoes).itervalues( ) ) #Conta a quantidade de vezes que cada elemento de Y aparece e gera um dicionário com o nome do elemento e a quantidade de valores que ele aparece. Recupera somente o 'valor' do dicionário através do itervalues(). Recupera o maior valor através do max()
taxa_de_acerto_base = 100.0 * acerto_base / len( teste_marcacoes )
print( "Taxa de acerto base: %f" % taxa_de_acerto_base )