def main():
    cat = int(input("Introduce categoría:"))
    
    if(cat >= 1 and cat <= 4):
        sueldo = float(input("Introduce sueldo:"))
        if (cat ==1):
            nuevo = sueldo*.15 + sueldo
        elif( cat ==2):
            nuevo = sueldo*.10 + sueldo
        elif( cat ==3):
            nuevo = sueldo*.08 + sueldo
        elif( cat ==4):
            nuevo = sueldo*.07 + sueldo
            
        print("Sueldo nuevo es: ", nuevo)
    else:
        print("Debe ser una número de categoría válido")

if __name__ == "__main__":
    main()