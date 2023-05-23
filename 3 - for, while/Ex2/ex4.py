import math

#Comandos de entrada
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
numero = 0

print ("")
print ("Os números primos para este intervalo [{}, {}] são: ".format (n1, n2))

#Comando for para a variável "a" no intervalo n1 ao n2+1
for a in range (n1, n2+1) :
	if a > 1:
		
		#O "j" vai de 2 até o "a" e verifica se é divisível por estes números
		for j in range (2, a) :
			if (a % j == 0) :
				
				#Se for divisível, break
				break
		
		#Se não for divisível, imprime a variável "a", pois este número é primo
		else :
			print (a)
		
		
