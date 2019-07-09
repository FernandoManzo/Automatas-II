# Nombre: lexico.py
# Objetivo: Script para analizar ñéxicamente la sentencia printf en ASCI C
# Author: Fernando Manzo Virgen
# 06/07/2019
cadena = []
aux2 = []
aux = ""
conts = True

def lexico(inst):
	c = 0
	lg = len(inst)
	while c < lg:
		cadena.append(inst[c])
		c += 1
	print(cadena)
	puntoComa()
	reservada()
	apertura()
	cerradura()
	comillas()

def puntoComa():
	v = (len(cadena))-1
	if (cadena[v] != ";"):
		print("**Error: falta definir ; al final de la sentencia")

def reservada():
	if len(cadena[0:6]) >= 6:
		aux = "".join(cadena[0:6])
		if (aux != "printf"):
			conts = True
		else:
			conts = False
	else:
		print("**Error: no es una palabra reservada: ingrese una instrucción más completa")


def apertura():
	if(conts != True):
		print ("**Error: no es una palabra reservada")
	else:
		try:
			aux = "".join(cadena[0:6])
			if (cadena[6] != "("):
				print ("**Error: no tiene definido en símbolo de apertura")
		except Exception:
			print("**Error: no tiene definido en símbolo de apertura")


def cerradura():
	v = (len(cadena))-2
	if (cadena[v] != ")"):
		print ("**Error: no tiene definido en símbolo de cerradura")

def comillas():
	comilla = 0
	c =0 
	a = '"'
	while c < len(cadena):
		if cadena[c]== a:
			comilla += 1
		c += 1
	texto(comilla)

def texto(c):
	const = 0
	a = '"'
	if c == 2:
		while const < len(cadena):
			if cadena[const] == a:
				x = (len(cadena))-4
				while const < x:
					const += 1
					aux2.append(cadena[const])
			const += 1
		const += 1
		imprimir(aux2)
	elif c==1:
		print("**Error: Falta definir una comilla")

	else:
		print("**Error: No se definieron las comillas")
	

def imprimir(aux2):
	valor = "".join(aux2)
	print("**Resultado: ",valor)


def main():
    print("-- Análisis léxico de la sentencia printf --")
    sentencia = input("Introduce la sentencia con printf: ")
    lexico(sentencia)


if __name__ == "__main__":
	main()