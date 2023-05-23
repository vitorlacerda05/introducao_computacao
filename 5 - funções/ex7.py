import math

#função que transforma rad em graus no intervalo 0-360
def g():
	rad = float(input("Digite o valor em radianos (0 até 6,28 (2pi)): "))
	graus = rad * (180/math.pi)
	return (rad, graus)

#saída de dados
(rad, graus) = g()
print("{} radianos equivale a {:.0f}°".format(rad, graus))
	
