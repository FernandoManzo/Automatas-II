import math as mat

class Punto(object):
    #Constructor de la clase
    def __init__(self, valorX, valorY):
        self.x = valorX
        self.y = valorY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, valorX):
        self.x = valorX
    
    def setY(self, valorY):
        self.y = valorY
        
    def toString(self):
        return "El punto tiene las siguientes coordenandas: ", self.x, ",", self.y

class Circunferencia(Punto):
    #Constructor de la clase
    def __init__(self, valorRadio):
        self.radio = valorRadio
    
    def getRadio(self):
        return self.radio
    
    def setRadio(self, valorRadio):
        self.radio = valorRadio
    
    def getArea(self):
        return mat.pi*mat.pow(self.getRadio(), 2)

    def toString(self):
        return "La circunferencia tiene como centro: ", self.getX(), ",", self.getY(), self.getRadio(),"El área es: ", self.getArea()
#Escriba la clase Clilindro  que hereda de Circunferencia, crea un objeto p4 y crea un método para calcular el geVolumen

class Cilindro(Circunferencia):
    def __init__(self, valorAltura):
        self.altura = valorAltura

    def getAltura(self):
        return self.altura

    def setAltura(self, valorAltura):
        self.altura = valorAltura

    def getVolumen(self):
        return self.getArea() * self.getAltura()

    def toString(self):
        return "El cilindro tiene un area: ", self.getArea(), "Una altura: ", self.getAltura(), "EL volumen es: ", self.getVolumen()


def main():
    #Programa principal

    #Creamos el objeto p1
    p1 = Punto(2,3)
    print(p1.toString())

    #Creamos el objeto p2
    p2 = Punto(0,0)
    print(p2.toString())

    #Invocamos el método set
    p2.setX(-2)
    p2.setY(-4)
    print(p2.toString())

    p3 = Circunferencia(12.34)
    p3.setX(10)
    p3.setY(12)

    print(p3.toString())

    p4 = Cilindro(9.81)
    p3.setX(2)
    p3.setY(2)
    p4.setRadio(3.12)
    print(p4.toString())


if __name__ == "__main__":
    main()