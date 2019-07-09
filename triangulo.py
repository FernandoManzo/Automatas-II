# Nombre: triangulo.py
# Objetivo: identificar que tipo de triangulo es
# math
# Author: Fernando Manzo Virgen
# 01/007/2019

def indentificar(l1, l2, l3):
	if(l1 == l2 and l1 == l3):
		print("El triángulo es equilatero", l1,",",l2,",",l3)
	elif(l1 != l2 and l1 != l3 and l2 != l3):
		print("El triángulo es escaleno", l1,",",l2,",",l3)
	else:
		print("El triángulo es isoceles", l1,",",l2,",",l3)

def perimetro(l1,l2,l3):
	p = l1+l2+l3
	print("El perimetro es: ", p)

def main():
	ciclo = True
	while ciclo == True:
		print("-- Identificar triángulo  --")
		l1 = float(input("Primer lado: "))
		l2 = float(input("Segundo lado: "))
		l3 = float(input("Tercer lado: "))
		indentificar(l1,l2,l3)
		perimetro(l1,l2,l3)

		resp = input("Otro cálculo (s/n)? ")
		if (resp == "S" or resp == "s"):
			ciclo = True
		else:
			ciclo = False


if __name__ == "__main__":
	main()