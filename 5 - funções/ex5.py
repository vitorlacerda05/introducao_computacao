import math

#função para verificar se é bissexto
def d():
	ano = int(input("Digite o ano para verificar se é bissexto: "))
	if ((ano % 100 == 0 and ano % 4 == 0 and ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)) :
		print("True")
	else :
		print("False")
	return

#chamar a função
d()
		
