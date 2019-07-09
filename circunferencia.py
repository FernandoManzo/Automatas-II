# Nombre: funciones.py
# Objetivo: calculo el áres y perimetro de una circunferencia
# math
# Author: Fernando Manzo Virgen
# 01/007/2019

import math as mat
import os

# -------------------------------
# Funión para calcular area 
# -------------------------------
def calculaArea(r):
	area = mat.pi*(mat.pow(r, 2))
	return area

def caculaDiamtero(r):
	diam = r * 2
	return diam

def main():
	ciclo  = True
	while ciclo == True:
		print("-- Sript para calcular área de circunferencia --")
		radio = float(input("Introduce el valor del radio: "))
		# invocar un método
		print ("El área: ", calculaArea(radio))
		print ("El diametro es: ", caculaDiamtero(radio))

		resp = input("Desea otro calculo? (s/n) ")
		if(resp == "S" or resp == "s"):
			ciclo = True
		else:
			ciclo = False
		#Borrar pantalla
		os.system("cls")
	else:
		print("\n")
		print("**Fin del programa")


if __name__ == "__main__":
	main()