import math

#Entrada de dados - em string
h1 = input("Horas que chegou (ex: 13 40): ")
h2 = input("Horas que saiu (ex: 14 50): ")

#Transformar de string para int, em determinado intervalo, para as horas:
hchegada = int(h1[0:2])
hsaida = int(h2[0:2])

#Transformar de string para int, em determinado intervalo, para os minutos:
mchegada = int(h1[3:5]) 
msaida = int(h2[3:5])

#Calcular horas e tempo final em minutos
if hsaida > hchegada :
	hf = hsaida - hchegada
	tempo = hf + ((msaida - mchegada) / 60)
	
else:
	hf = 24 + (hsaida - hchegada)
	tempo = hf + ((msaida - mchegada) / 60)

print ("O tempo que você ficou foi de {}h".format(tempo))

#Calculo do valor a pagar
if tempo <= 1 :
	print("O valor a ser pago é de R$ 1,00")

elif tempo > 1 and tempo <= 2:
	print("O valor a ser pago é de R$ 2,00")
	
elif tempo > 2 and tempo <= 3:
	print("O valor a ser pago é de R$ 3,40")

elif tempo > 3 and tempo <= 4:
	print("O valor a ser pago é de R$ 4,80")

else :
	valor = (tempo // 1) * 2
	print("O valor a ser pago é de R$ {}".format(valor))
