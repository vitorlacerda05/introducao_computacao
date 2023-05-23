import math

#comandos de entrada
htrab = float(input ("Digite o valor da hora trabalhada, em reais: "))

hmes = float(input ("Digite o numero de horas trabalhadas no mês: "))

#formula do valor
valor = htrab * hmes * 1.1

#comando if

if valor <= 2800.00:
	imposto = valor * 0.03

else :
	imposto = valor * 0.05
	
# comando de saída
print ("O valor a ser pago para o seu funcionário, que trabalhou durante {} horas no mês, por {}R$ reais a hora, é {:.2f}R$.".format(htrab, hmes, valor - imposto))
