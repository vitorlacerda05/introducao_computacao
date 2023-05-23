import math

#Entrada de dados
valor = float(input("Digite o valor emprestado: "))
pago = float(input("Digite o valor que deseja pagar mensalmente: "))
juros = float(input("Digite o valor do juros (%): "))

#Atribuição de valores para variáveis
sobra = pago
jurostotal = 0

#Comando while quando sobra for maior que o valor pago
while sobra >= pago :
	jurosmes = valor * (juros / 100)
	sobra = ( jurosmes + valor ) - pago
	print("Total: {:.2f}  Juros: {:.2f}  Pagamento: {:.2f}  Sobra: {:.2f} ".format(valor, jurosmes, pago, sobra))
	valor = sobra
	
	jurostotal += jurosmes
	
	jurosmes = valor * (juros / 100)
	
	#Comando if para quando a (sobra + jurosmes) for menor que o valor pago
	if (sobra + jurosmes) < pago :
		jurostotal += jurosmes
		pago = jurosmes + valor
		sobra = 0.0
		print("Total: {:.2f}  Juros: {:.2f}  Pagamento: {:.2f}  Sobra: {:.2f} ".format(valor, jurosmes, pago, sobra))

#Impressão dos juros totais
print ("Juros totais: {:.2f}".format(jurostotal))
