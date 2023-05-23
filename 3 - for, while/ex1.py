import math

#Entrada de dados
n = int(input("Digite o número de elementos da sequencia Fibonacci: "))

#Atribuição de valores para variáveis
prox = 1
ant = 0

for i in range(0, n) :
	
	print(prox)
	
	#Formula do Fibonacci
	
	prox = prox + ant
	ant = prox - ant
	
