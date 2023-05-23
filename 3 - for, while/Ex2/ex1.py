import math

#Atribuição da função e sua derivada
f = lambda x: x ** 3 - x ** 2 - 13 * x + 8
f1 = lambda x: 3 * x ** 2 - 2 * x - 13
passo = lambda y: y - f(y) / f1(y)

#Entrada de valores
x0 = float(input("Digite a aproximação inicial: "))
it1 = 0
it2 = float(input("Digite o numero de iterações para calcular a raiz: "))

#Comando while
while it1 <= it2 :
	x1 = passo(x0)
	x0 = x1
	it1 += 1

#Saída de valores
print ("A raiz da função encontrada é x = {}".format(x1))
