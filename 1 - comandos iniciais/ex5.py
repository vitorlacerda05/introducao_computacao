import math

#Comando de entrada
x = float(input("Escreva o valor de x para calcular o seu seno, em radianos e no intervalo 0 a pi/2: "))

#Formulas
sx = x - ((x ** 3)/math.factorial(3)) + ((x ** 5)/math.factorial(5)) - ((x ** 7)/math.factorial(7)) + ((x ** 9)/math.factorial(9))

spx = math.sin(x)

#Comando de saída
print("O valor do sen({}) calculado pela série de Taylor é {}, já o valor da função padrão do Python é {}".format(x,sx, spx))
