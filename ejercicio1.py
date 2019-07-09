# Nombre: ejercicio1.py
# Objetivo: 
# programa en Python que dado como dato el sueldo de un trabajador, 
# le aplique un aumento del 15% si su sueldo es inferior a $1000.00 y del 12%
# Author: Fernando Manzo Virgen
# 04/07/2019

def main():
    st = float(input("Introduce sueldo:"))
    
    if(st < 1000):
        sf = st*.15 + st
    elif( st >= 1000):
        sf = st*.12 + st
    print("Sueldo final es: ", sf)

if __name__ == "__main__":
    main()