import math

#Irei computar a raiz da função f(t) = t ** 3 - t ** 2 - 13 * t + 8 com tolerância de 0.0001
print("------------------------------------------------------------------------------")
print("---------- Programa que verifica se o método proposto calcula a raiz ---------")
print("----da função f = x ** 3 - x ** 2 - 13 * x + 8, com a tolerância de 0.0001----")
print("------------------------------------------------------------------------------")
print("")

#Atribuição de valores e determinação da função
a = 0
f = lambda t: t ** 3 - t ** 2 - 13 * t + 8
t = a

#Impressão do valor inicial do intervalo
print("O valor inicial do intervalo é",a)
print("")

#Encontrar o intervalo de tamanho [0, 1] no qual a raiz está localizada - com comando FOR
for t in range(a, 9999, 1) :
    y = f(t)
    if y < 0 :
        print("O intervalo de tamanho [0, 1] é: [{}, {}]". format(t-1, t))
        break

#Encontrar o intervalo de tamanho [0.0, 0.1] no qual a raiz está localizada - com comando WHILE
t= t-1.1
y = 0
while y >= 0 :
    t += 0.1
    y = f(t)
    
print("O intervalo de tamanho [0, 0.1] é: [{:.1f}, {:.1f}]". format(t-0.1, t))

#Encontrar o intervalo de tamanho [0.1, 0.01] no qual a raiz está localizada - com comando WHILE
t= t-1.01
y = 0
while y >= 0 :
    t += 0.01
    y = f(t)
    
print("O intervalo de tamanho [0.1, 0.01] é: [{:.2f}, {:.2f}]". format(t-0.01, t))

#Encontrar o intervalo de tamanho [0.01, 0.001] no qual a raiz está localizada - com comando WHILE
t= t-1.001
y = 0
while y >= 0 :
    t += 0.001
    y = f(t)
    
print("O intervalo de tamanho [0.01, 0.001] é: [{:.3f}, {:.3f}]". format(t-0.001, t))

#Encontrar o intervalo de tamanho [0.001, 0.0001] no qual a raiz está localizada - com comando WHILE
t= t-1.0001
y = 0
while y >= 0 :
    t += 0.0001
    y = f(t)
    
print("O intervalo de tamanho [0.001, 0.0001] é: [{:.4f}, {:.4f}]". format(t-0.0001, t))

#Encontrar o intervalo de tamanho [0.0001, 0.00001] no qual a raiz está localizada - com comando WHILE
t= t-1.00001
y = 0
while y >= 0 :
    t += 0.00001
    y = f(t)

print("O intervalo de tamanho [0.0001, 0.00001] é: [{:.5f}, {:.5f}]". format(t-0.00001, t))

#Impressão de valores finais e verificação se o método funciona
print("")
print("A raiz da função f = x ** 3 - x ** 2 - 13 * x + 8, com a tolerância de 0.0001 é {:.5f}". format(t-0.00001))
print("E este método realmente funciona!")
