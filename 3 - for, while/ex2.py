import math

#Entrada de valores e atribuição de variáveis
frase = str(input("Escreva uma frase: "))
letra = str(input("Escreva a letra para verificar o número de vezes que aparece: "))
n = 0

#Comando for
for i in frase :
	if i == letra :
		n = n + 1

#Saida de dados
print("A letra {} apareceu {} vezes na frase". format(letra, n))
