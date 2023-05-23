import math

#definição da função e entrada de dados
def s():
	salario = float(input("Digite o valor do seu salário: "))
	
	#comandos if para o calculo do imposto de renda
	if salario > 2500.00 and salario <= 3200.00 : 
		i = salario * 0.075
		
	elif salario > 3200.00 and salario <= 4250.00:
		i = salario * 0.15
		
	elif salario > 4250.00 and salario <= 5300.00:
		i = salario * 0.225
		
	else :
		i = salario * 0.275
	
	return (salario, i)

#saída de dados
(salario,i) = s()
if salario <= 2500 :
	print ("Você está isento de impostos em seu salário!")
	
if salario > 2500 :
	print ("O valor do imposo a ser recolhido na fonte é {}".format(i))
