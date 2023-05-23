import math

#Definição das funções
def s():
	somasen = 0
	for i in range(n):
		seno = ((-1) ** i / math.factorial (2 * i + 1)) * rad ** (2 * i + 1)
		somasen += seno 
	return somasen
	
def c():
	somacos = 0
	for i in range(n):
		cos = ((-1) ** i / math.factorial (2*i)) * rad **(2 * i)
		somacos += cos
	return somacos
	
def t():
	somacos = c()
	somasen = s()
	tg = somacos/somasen
	return tg

#Entrada de dados
rad = float(input("Digite o valor do angulo em rad (0 até pi/2): "))
n = int(input("Digite o número de séries: "))

#Atribuição de valores a variáveis e chamada de função
i = 0
somacos = c()
somasen = s()
tg = t()

#Saída de dados
print("")
print("Valor do seno é {:.4f}".format(somasen))
print("Valor do cosseno é {:.4f}".format(somacos))
print("Valor da tangente é {:.4f}".format(tg))

