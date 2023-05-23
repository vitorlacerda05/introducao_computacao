import math

#Entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#Comandos IF para verificar qual número é o maior e qual é menor
if n1 > n2 and n1 > n3 :
	print("O primeiro número é o maior")
	
	if n2 > n3 :
		print("O terceiro número é o menor")
	
	else : 
		print("O segundo número é o menor")

if n2 > n1 and n2 > n3 :
	print("O segundo número é o maior")
	
	if n1 > n3 :
		print("O terceiro número é o menor")
	
	else : 
		print("O primeiro número é o menor")

if n3 > n1 and n3 > n2 :
	print("O terceiro número é o maior")
	
	if n1 > n2 :
		print("O segundo número é o menor")
	
	else : 
		print("O primeiro número é o menor")

if n1 == n2 and n2 == n3 :
	print("Todos os números são iguais")
