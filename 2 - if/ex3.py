import math
import random

x = random.randint(0, 100)

# Comando de entrada

y1 = int(input("Digite numeros inteiros de 0 a 100 para descobrir o numero gerado: "))

# 9 chances

if y1 > x :
	y2 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 9 chances: "))

elif y1 < x :
	y2 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 9 chances: "))
	
elif y1 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 8 chances

if y2 > x :
	y3 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 8 chances: "))

elif y2 < x :
	y3 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 8 chances: "))
	
elif y2 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()
# 7 chances

if y3 > x :
	y4 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 7 chances: "))

elif y3 < x :
	y4 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 7 chances: "))
	
elif y3 == x :  
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 6 chances

if y4 > x :
	y5 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 6 chances: "))

elif y4 < x :
	y5 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 6 chances: "))
	
elif y4 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 5 chances

if y5 > x :
	y6 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 5 chances: "))

elif y5 < x :
	y6 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 5 chances: "))
	
elif y5 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 4 chances

if y6 > x :
	y7 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 4 chances: "))

elif y6 < x :
	y7 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 4 chances: "))
	
elif y6 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 3 chances

if y7 > x :
	y8 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 3 chances: "))

elif y7 < x :
	y8 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 3 chances: "))
	
elif y7 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 2 chances

if y8 > x :
	y9 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 2 chances: "))

elif y8 < x :
	y9 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 2 chances: "))
	
elif y8 == x :  
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# 1 chance

if y9 > x :
	y10 = int(input("O numero que você digitou é maior que o numero gerado, tente novamente, você possui mais 1 chances: "))

elif y9 < x :
	y10 = int(input("O numero que você digitou é menor que o numero gerado, tente novamente, você possui mais 1 chances: "))
	
elif y9 == x : 
	print("Você acertou o numero {}, parabéns!".format(x))
	exit()

# Resultado final

if y10 > x :
	print("Você não acertou o numero {} gerado nas 10 tentativas!".format(x))

elif y10 < x :
	print("Você não acertou o numero {} gerado nas 10 tentativas!".format(x))
	
elif y10 == x : 
	print("Você acertou o numero {} gerado na última tentativa, parabéns!".format(x))
