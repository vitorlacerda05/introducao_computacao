import math

#Entrada de dados
h = int(input("Digite a altura de seu reservatório, em centimetros: "))
l = int(input("Digite a largura de seu reservatório, em centimetros: "))
c = int(input("Digite a comprimento de seu reservatório, em centimetros: "))

consumo = int(input("Digite o comsumo médio diário, em litros/dia: "))

#Formulas de capacidade e autonomia
capacidade = ( h * l * c ) * 0.001

print ("A capacidade de seu reservatório é de {}L".format(capacidade))

autonomia = capacidade / consumo

print ("A autonomia de seu reservatório é de {} dias".format(autonomia))

#Comandos IF
if autonomia < 2.0 :
	print("Consumo elevado")
	
elif autonomia >= 2 and autonomia <= 7 :
	print("Consumo moderado")
	
else :
	print("Consumo reduzido")
