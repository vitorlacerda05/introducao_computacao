import math

#Formulas funções
f = lambda x: (x ** 3) - (x ** 2) - (13 * x) + 8
f1 = lambda x: (3 * x ** 2) - (2 * x) - 13

#Comando de entrada
x0 = float(input("De um chute inicial para a raiz da função: "))

#Iterações usando o método de Newton-Raphson
x1 = x0 - f(x0) / f1(x0)

x2 = x1 - f(x1) / f1(x1)

passo = lambda y: y - f(y) / f1(y)

x3 = passo(x2)

x4 = passo(x3)

x5 = passo(x4)

x6 = passo(x5)

x7 = passo(x6)

x8 = passo(x7)

x9 = passo(x8)

x10 = passo(x9)

#Comando de saída
print("A raiz da função para o chute inicial {}, é {}".format(x0, x10))
