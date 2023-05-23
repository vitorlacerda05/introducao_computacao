import math

#Entrada de dados
v1 = int(input("Digite o valor inicial: "))
v2 = int(input("Digite o valor final: "))
razao = int(input("Digite a razão: "))
soma = 0

#Comando for
for i in range(v1, v2, razao) :
	print (i)
	soma = soma + i

#Copmando de saída	
print ("Valor da soma: ", soma)
