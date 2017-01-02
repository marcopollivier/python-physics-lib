from sys import *

def lei_coulomb(carga, carga_prova, distancia):
	k = 8.99 * (10**-19)
	return (k * carga * carga_prova) / (distancia**2)
