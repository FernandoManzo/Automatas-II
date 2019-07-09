# Nombre: fibonacci.py
# Objetivo: fibonacci de un número
# math
# Author: Fernando Manzo Virgen
# 01/07/2019

#importar la liberia math
import math as mat

#Metodo para optener fibonacci
def fibonacci(n):
	var1 = 1
	var2 = 0
	c = 0
	while c<n:
		fib = var1 + var2
		var1 = var2
		var2 = fib
		print("Número: ", fib)
		c += 1 

def main():
	ciclo = True
	while ciclo == True:
		print("----------- Fibonacci -----------")
		numero = int(input("Ingrese número para optener fibonacci: "))
		fibonacci(numero)

		resp = input("Desea otro calculo? (s/n) ")
		if(resp == "S" or resp == "s"):
			ciclo = True
		else:
			ciclo = False


if __name__ == "__main__":
	main()