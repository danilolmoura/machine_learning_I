#coding: utf-8

#Abordagem
#1. Separar 90% do arquivo para treinar o algoritmo, e 10% para testá-lo

from dados 				 import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

X, Y = carregar_acessos()

treino_dados 	 = X[:90] #Devolve as 90 primeiras posições de X
treino_marcacoes = Y[:90] #Devolve as 90 primeiras posições de Y
teste_dados      = X[-9:] #Devolve as últimas 9 linhs  de X
teste_marcacoes  = Y[-9:] #Devolve as últimas 9 linhas de Y


modelo = MultinomialNB()
modelo.fit( treino_dados, treino_marcacoes ) #Treina o algoritmo utilizando as combinações e suas respectivas respostas

resultado = modelo.predict( teste_dados ) #Utiliza o modelo já treinado para 'prever' o resultado dos valores reservados para testes.

diferencas = resultado - teste_marcacoes #Compara a resposta dada pelo modelo com as respostas corretas.
acertos    = [d for d in diferencas if d==0] #Recupera somente as respostas acertadas pelo modelo

total_de_acertos = len(acertos) 
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos #Calcula a porcentagem de acertos do modelo


print(taxa_de_acerto)
print(total_de_elementos)
