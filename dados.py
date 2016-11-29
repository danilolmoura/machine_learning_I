import csv

def carregar_acessos( ):
	X = [] #Comportamentos conhecidos
	Y = [] #Resultados dos comportamentos conhecimentos

	arquivo = open( 'csv/acesso.csv', 'rb' )
	leitor  = csv.reader( arquivo )
	leitor.next( ) #ignora a primeira linha

	for home, como_funciona, contato, comprou in leitor:
		dado = [int(home), int(como_funciona), int(contato)]
		
		X.append( dado )
		Y.append( int(comprou) )

	return X, Y

def carregar_buscas( ):
	X = [] 
	Y = []

	arquivo = open( 'csv/busca.csv', 'rb' )
	leitor  = csv.reader( arquivo )
	leitor.next( ) #ignora a primeira linha

	for home, busca, logado, comprou in leitor:
		dado = [int(home), busca, int(logado)]
		
		X.append( dado )
		Y.append( int(comprou) )

	return X, Y