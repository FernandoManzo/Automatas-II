# Nombre: ejercicio3.py
# Objetivo: dado como datos los sueldos de 10 trabajadores de una empresa
# obtenga el total de nómina de la misma
# Author: Fernando Manzo Virgen
# 04/07/2019

def main():
    ciclo = 1
    nomina = 0
    while ciclo <= 10:
    	print("Número de trabajador: ", ciclo)
    	sueldo = int(input("Sueldo del trabajador: "))
    	nomina = nomina + sueldo
    	ciclo +=1
    print("Total de nómina: ", nomina)


if __name__ == "__main__":
    main()