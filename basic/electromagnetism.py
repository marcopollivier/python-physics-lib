from sys import *

def lei_coulomb(carga, carga_prova, distancia):
	k = 8.99 * (10**-19)
	return (k * carga * carga_prova) / (distancia**2)

#Perguntando ao usuário as informações necessárias
carga = input("Qual a carga (Q) ?")
carga_prova = input("Qual a carga de prova (q) ?")
distancia = input("Qual a distancia (d) ?")

saida = "A força encontrada é %s." % (lei_coulomb(carga, carga_prova, distancia))

print(saida)

