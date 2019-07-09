# Nombre: ejercicio4.py
# Objetivo: que permita capturar en una lista las calificaciones de N alumnos y que le permita calcular e imprimir
# Author: Fernando Manzo Virgen
# 04/07/2019

lista = []

def agregarCalf(calf):
	lista.append(calf)

def promedio():
	num = len(lista)
	c = 0
	suma = 0
	while c< num:
		suma = suma + lista[c]
		c += 1

	promedio = suma / num
	print ("*El promedio es: ", promedio)

def aprobados_reprobados():
	num = len(lista)
	c = 0
	reprobado = 0
	aprobado = 0
	while c< num:
		if (lista[c] < 70):
			reprobado += 1
			c += 1
		else:
			aprobado +=1
			c += 1
	print("**Aprovados: ", aprobado)
	print("**Reprobado: ", reprobado)

def porcentaje():
	num = len(lista)
	c = 0
	reprobado = 0
	aprobado = 0
	while c< num:
		if (lista[c] < 70):
			reprobado += 1
			c += 1
		else:
			aprobado +=1
			c += 1
	pAprobados = (aprobado * 100) / num
	pReprobados = (reprobado * 100) / num
	print("**Porcentaje Aprovados: ", pAprobados)
	print("**Porcentaje Reprobados: ", pReprobados)

def mayor():
	num = len(lista)
	c = 0
	cuenta = 0
	while c< num:
		if (lista[c] > 80):
			cuenta += 1
			c += 1
		else:
			c += 1
	print("**Alumnos con promedio mayor a 80: ", cuenta)

def main():
	ciclo = True
	while ciclo == True:
		print("----- Script para trabajar con listas -----")
		print("1.- Agregar calificacion de alumno")
		print("2.- Promedio general")
		print("3.- No. de alumnos aprobados y reprobados ")
		print("4.- Porcentaje de alumnos aprobados y reprobados ")
		print("5.- Número de alumnos cuya calificación fue mayor a 80 ")
		print("6.- Salir ")
		print("--------------------------------------------------------")

		opc = int(input("Elija una opción entre 1 y 6: "))

		if( opc == 1):
			calf = int(input("Introduce la calificación: "))
			agregarCalf(calf)
		elif (opc == 2):
			promedio()
		elif (opc == 3):
			aprobados_reprobados()
		elif (opc == 4):
			porcentaje()
		elif (opc == 5):
			mayor()
		elif (opc == 6):
			print("** Fin del programa")
			ciclo = False

		else:
			print("Selecciona un entero entre 1 y 6")

if __name__ == "__main__":
    main()