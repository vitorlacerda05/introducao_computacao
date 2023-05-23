import math

#entrada do graus celsius
c = input("digite a temperatura em graus Celsius: ")

#formula farenheit
f = ( float(c) * (9.0 / 5.0) ) + 32.0

#comando de saida
print("{:.3f} graus celsius equivale a {:.3f} graus farenheit".format(c, f))
