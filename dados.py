import csv

def carregar_acessos( ):
	X = [] #Comportamentos conhecidos
	Y = [] #Resultados dos comportamentos conhecimentos

	arquivo = open( 'acesso_pagina.csv', 'rb' )
	leitor  = csv.reader( arquivo )
	leitor.next( ) #ignora a primeira linha

	for home, como_funciona, contato, comprou in leitor:
		dado = [int(home), int(como_funciona), int(contato)]
		
		X.append( dado )
		Y.append( int(comprou) )

	return X, Y