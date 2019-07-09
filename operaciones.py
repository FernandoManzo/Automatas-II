# Nombre: funciones.py
# Objetivo: muestra como trabajan los métodos o funciones en python
# Author: Fernando Manzo Virgen
# Fecha: 29/06/2019

#------------------------------------------------------------------
# Función para sumar dos enteros
#------------------------------------------------------------------
def suma(num1,num2):
	return num1+num2
#------------------------------------------------------------------
# Función para restar dos enteros
#------------------------------------------------------------------
def resta(num1,num2):
	return num1-num2
#------------------------------------------------------------------
# Función para multiplicar dos enteros
#------------------------------------------------------------------
def multiplica(num1,num2):
	return num1*num2
#------------------------------------------------------------------
# Función para dividir dos enteros
#------------------------------------------------------------------
def divide(num1,num2):
	return num1/num2
#------------------------------------------------------------------
# Función para comparar dos enteros
#------------------------------------------------------------------
def compara(num1,num2):
	if(num1>num2):
		print("El mayor es num1", num1)
	elif(num2>num1):
		print("El mayor es num2", num2)
	else:
		print("Los números son iguales", num1, ",", num2)
#------------------------------------------------------------------
# Función para hacer un ciclo for
#------------------------------------------------------------------
def cuenta(num1, num2):
	if (num2>num1):
		for i in range(num1, num2+1):
			print("Valor de i", i)
	
	if(num1>num2):
		for i in range(num2, num1-1):
			print("Valor de i-", i)





#Función main
def main():
	ciclo= True
	while (ciclo == True):
		print("---Operaciones básicas---")
		print("\n")
		n1 = int(input("Introduce primer número: "))
		n2 = int(input("Introduce segundo número: "))

		# Invocamos las funciones
		print("La suma es: " + str(suma(n1, n2)))
		print("La resta es: " + str(resta(n1, n2)))
		print("La multiplicación es: " + str(multiplica(n1, n2)))
		print("La división es: " + str(divide(n1, n2)))
		compara(n1,n2)
		cuenta(n1,n2)

		cad = input("Otro cálculo (s/n?")
		if (cad == "S" or cad == "s"):
			ciclo = True
		else:
			ciclo = False



if __name__ == "__main__":
	main()



