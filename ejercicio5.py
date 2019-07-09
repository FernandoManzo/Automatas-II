# Nombre: ejercicio5.py
# Objetivo: que permita almacenar en un diccionario los datos generales de un alumno del ITC.
# Deberá poder imprimir cada uno de éstos datos a través de la clave del
#diccinario y modificar al menos uno de los datos (ej. número telefónico).
# Author: Fernando Manzo Virgen
# 04/07/2019
lista = {
	"nombres":"Fernando",
    "apellidos":"Manzo",
    "telefono":"3121740217",
}

def imprimir():
	print("-------------------------------")
	for clave, valor in lista.items():
		print(clave + ": " + valor)
	print("-------------------------------")


def modificar(n, r):
	for clave in lista.keys():
		if (clave == n and r==1):
			a = input("Ingrese nuevo valor: ")
			lista[n]=a;
			imprimir()
		elif(clave == n and r==2):
			print(lista[n])

def main():
	ciclo = True
	while ciclo == True:
		imprimir()
		print("1.- Desea modificar")
		print("2.- Desea imprimir")
		r = int(input("Elija una opción (1/2): "))
		print("--------------------------------")
		print("¿Qué atributo desea?")
		print("1.-Nombre")
		print("2.-Apellidos")
		print("3.-Telefono")
		opc = int(input("Elije una oción: "))
		if (opc == 1):
			n = "nombres"
			modificar(n, r)
		elif (opc == 2):
			n = "apellidos"
			modificar(n, r)
		elif (opc == 3):
			n = "telefono"
			modificar(n, r)

		otra = input("Desea otra operación: ")
		if (otra == "S" or otra == "s"):
			ciclo = True
		else:
			ciclo = False

if __name__ == "__main__":
    main()