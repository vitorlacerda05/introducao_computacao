import math

# Comando de entrada salário
salario = float (input("Digite o valor do seu salário: "))

#Comandos IF
if salario <= 2500.00 :
	
	print ("Você está isento de impostos em seu salário!")
	
elif salario > 2500.00 and salario <= 3200.00 : 
	i = salario * 0.075
	
	print ("O valor do imposo a ser recolhido na fonte é {}".format(i))
	
elif salario > 3200.00 and salario <= 4250.00:
	i = salario * 0.15
	
	print ("O valor do imposo a ser recolhido na fonte é {}".format(i))
	
elif salario > 4250.00 and salario <= 5300.00:
	i = salario * 0.225
	
	print ("O valor do imposo a ser recolhido na fonte é {}".format(i))
	
else :
	i = salario * 0.275
	
	print ("O valor do imposo a ser recolhido na fonte é {}".format(i))
