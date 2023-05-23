import math

# importar dados
sexo = str(input("Digite o seu sexo (M/F): "))
altura = float(input ("Digite a sua altura: "))

# estruturas do if
if sexo == "m" : 
	pi = (72.7 * altura) - 58
	print ("Seu peso ideal é {:.3f} ".format(pi))

else :
	pi = (62.1 * altura) - 44.7
	print ("Seu peso ideal é {:.3f} ".format(pi))
