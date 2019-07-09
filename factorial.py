# Nombre: factorial.py
# Objetivo: factorial de un número
# math
# Author: Fernando Manzo Virgen
# 01/07/2019

#importar la liberia math
import math as mat

#Metodo para optener factorial
def factorial(n):
	if( n == 0):
		return 1
	else:
		return n * factorial(n-1)

def main():
	print("--- Factorial ---")
	numero = int(input("Ingrese número para optener factorial: "))
	print(factorial(numero))


if __name__ == "__main__":
	main()