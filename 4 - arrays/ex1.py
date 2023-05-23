import math

#Definir a lista e variáveis iniciais
s = input("Qual seu nome?: ")
n = input("Digite um número entre 1 e 10: ")
nomes = []
numeros = []

#Comando while para entrada de dados e adicionar na lista
while len(s) > 0 :
	nomes.append(s)
	s = input("Qual seu nome?: ")
	x = int(n)
	numeros.append(x)
	n = input("Digite um número entre 1 e 10: ")


#Saída dos dados que foram recebidos
print ("")
print ("Os nomes dos jogadores são:", nomes)
print ("Os numeros digitados pelos jogadores são:", numeros)

i = -2

while len(nomes) != 0:
		
	#Somar os números digitados
	print ("")
	soma = 0
	for x in numeros:
		soma = soma + x
	print ("A soma dos números digitados é:",soma)
	
	soma = soma - 1
	
	#Criar sublista com sequencia igual
	nomesf = soma * 10 * nomes
	
	#Pular jogadores
	i += 1
	f = i
	while i >= 0 :
		nomesf.pop(i)
		i = i - 1
	i = f	
	
	#Eliminar o jogador da soma
	eliminar = nomesf[(soma)]
	print("O jogador eliminado foi:", eliminar)
	posicao = nomes.index(eliminar) #para pegar a posição do jogador
	nomes.remove(eliminar)
	
	#Retirar o número do jogador da lista
	numeros.pop(posicao)
	
	print ("Os nomes dos jogadores restantes são:", nomes)
	
	if len(nomes) == 1:
		print ("")
		print ("O jogador vencedor é", nomes)
		break

