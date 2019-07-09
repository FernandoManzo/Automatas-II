# Nombre: calculadora.py
# Objetivo: calculadora básica
# Author: Fernando Manzo Virgen
# 06/07/2019

from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def producto():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()

def dividir():
    r.set( float(n1.get()) / float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")

# Configuración de la raíz
root = Tk()
root.title("Calculadora")
root.config(bd=30)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack()  # Separador

Button(root, text="Suma", command=sumar, fg="white", bg="green").pack(side="left")
Button(root, text="Resta", command=resta, fg="white", bg="orange").pack(side="left")
Button(root, text="Producto", command=producto, fg="white", bg="blue").pack(side="left")
Button(root, text="División", command=dividir, fg="white", bg="red").pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()