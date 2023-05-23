import math

# Comando de entrada
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))

# Formula
nf = ( n1 + n2 ) / 2

# Comandos IF
if nf >= 7.0 :
	print ("Sua nota final foi {}, aprovado!".format(nf))

elif nf < 7.0 and nf > 5.0 :
	print ("Sua nota final foi {}, recuperação!".format(nf))

else :
	print ("Sua nota final foi {}, reprovado!".format(nf))
