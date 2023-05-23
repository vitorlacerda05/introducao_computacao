import math

print("----- Pense em um número, entre 1 a 100, para o programa adivinhar qual é! -----")
print(" Você deve dizer se o número chutado é maior, menor ou igual ao que você pensou!")
print("")

#Importar random para gerar numeros aleatórios inicialmente entre 1 e 100 e atribuição de variáveis
import random
i = 1
f = 100
tentativas = 1
numero = random.randrange(1, 100)

#Comando while
while tentativas <= 999 :
	
	print("")
	#Impressão para o usuário e entrada de dados
	print("{}° tentativa. O número é {}? ".format (tentativas, numero))
	resposta = input(" Digite a sua resposta: ")
    
    #Caso a resposta for maior
	if resposta == "maior" :
		i = numero
		tentativas += 1
		numeroteste = random.randrange(i, f)
        
        #Este While corrige se o número gerado foi igual ao anterior
		while numeroteste == numero :
			numeroteste = random.randrange(i, f)
		
		numero = numeroteste

	#Caso a resposta for menor
	elif resposta == "menor" :
		f = numero
		tentativas += 1
		numeroteste = random.randrange(i, f)
		
		#Este While corrige se o número gerado foi igual ao anterior
		while numeroteste == numero :
			numeroteste = random.randrange(i, f)
		
		numero = numeroteste
			
	#Caso a resposta for igual, o programa acertou o numero
	elif resposta == "igual" :
		print("")
		print("O número que você pensou é {}!".format(numero))
		break

	#Caso o usuário digitou alguma resposta diferente 
	else:
		print(" Digite apenas 'maior', 'menor' ou 'igual'")
