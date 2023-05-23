import math

x = float(input("Digite o valor para calcular sua raiz quadrada: "))
x0 = float(input("Digite um chute inicial: "))

if x >= 0 :
	for k in range(0, 100) :
		xi = 1/2 *( x-1 - x / x0 )
		
		if ( xi - x ) < 0.00000001 :
			print("A raiz quadrada é aproximadamente igual a ", x0)
			break

