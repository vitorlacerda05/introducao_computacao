import math

#Entrada de dados
frase = str(input("Digite a frase: "))

#Atribuição de valores para variáveis
a = 0
e = 0
i = 0
o = 0
u = 0

#Comando for
for letra in frase : 
	if letra == "a" :
		a = a + 1
	
	elif letra == "e" :
		e = e + 1
		
	elif letra == "i" :
		i = i + 1
	
	elif letra == "o" :
		o = o + 1
		
	elif letra == "u" :
		u = u + 1

print ("As vogais A, E, I, O, U, aparecem, respectivamente, {}, {}, {}, {} e {} vezes.".format(a, e, i, o, u))
