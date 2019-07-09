# --------------------------------------------------------
# Nombre: listas.py
# Objetivo: muestra el funcionamiento de las listas en Python
# Author: Fernando Manzo Virgen
# Fecha: 02/07/2019
# --------------------------------------------------------

import os

# --------------------------------------------------------
# Creación de la lista
# --------------------------------------------------------
lista = []

# --------------------------------------------------------
# Función para agregar items a la lista
# --------------------------------------------------------
def agregarItem(dato):
	lista.append(dato)

# --------------------------------------------------------
# Función para imprimir items de la lista
# --------------------------------------------------------
def imprimirLista():
	j=0
	for i in lista:
		print("Item: ",j,",",i)
		j +=1

# --------------------------------------------------------
# Función para borrar items a la lista
# --------------------------------------------------------
def eliminarItem(dato):
	#Buscamos el item
	if(dato in lista):
		lista.remove(dato)
		print("**Item eliminado")
	else:
		print("**Item no existe en las lista")

def main():
	ciclo = True
	while ciclo == True:
		print("--- Script para trabajar con listas ---")
		print("1.- Agregar elementos a la lista ")
		print("2.- Buscar un elemento en la lista ")
		print("3.- Modificar un elemento en la lista ")
		print("4.- Eliminar un elemento en la lista ")
		print("5.- Imprimir los elementos de la lista ")
		print("6.- Salir ")

		opc = int(input("Elija una opción entre 1 y 6: "))

		if( opc == 1):
			item = input("Introduce el valor del item: ")
			agregarItem(item)
		elif (opc == 2):
			print("2")
		elif (opc == 3):
			print("3")
		elif (opc == 4):
			print("4")
		elif (opc == 5):
			imprimirLista()

		elif (opc == 6):
			print("** Fin del programa")
			ciclo = False

		else:
			print("Selecciona un entero entre 1 y 6")

	

if __name__ == "__main__":
	main()