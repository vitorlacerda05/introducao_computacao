import math

#Entrada de dados
dia = int(input("Digite o dia: "))

mes = int(input("Digite o mês: "))

ano = int(input("Digite o ano: "))

#Verificar se o ano digitado é o correto
if ano >= 1900 :
	
	#Ano bissexto
	if ((ano % 100 == 0 and ano % 4 == 0 and ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)) :
		if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
			if dia >= 1 and dia <= 31 :
				print("Data válida")
			else : 
				print("Data inválida")
		
		if mes == 2 :
			if dia >= 1 and dia <= 29 :
				print("Data válida")
			else : 
				print("Data inválida")

		if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
			if dia >= 1 and dia <= 30 :
				print("Data válida")
			else : 
				print("Data inválida")
		
		if mes < 1 or mes > 12 : 
			print("Data inválida")
	
	#Ano não bissexto
	else:	
		if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
			if dia >= 1 and dia <= 31 :
				print("Data válida")
			else : 
				print("Data inválida")
		
		if mes == 2 :
			if dia >= 1 and dia <= 28 :
				print("Data válida")
			else : 
				print("Data inválida")

		if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
			if dia >= 1 and dia <= 30 :
				print("Data válida")
			else : 
				print("Data inválida")
		
		if mes < 1 or mes > 12 : 
			print("Data inválida")

else : 
	print("Data inválida")
