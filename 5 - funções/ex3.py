import math

#definir função e retornar o peso
def peso() :
	if s == "H" or s == "h" :
		p = (72.7 * alt) - 58
		return p

	elif s == "M" or s == "m" :
		p = (62.1 * alt) - 44.7
		return p
	
	else :
		print("Digite corretamente seus dados")

#entrada de dados
alt = float(input("Digite sua altura: "))
s = input("Digite seu sexo (H/M): ")

#x obtem o valor retornado na função peso()
p = peso()

print ("O seu peso ideal é {:.3f}".format(p))
