from Vertice import Vertice
from Rectangulo import Rectangulo

print("Programa que crea rectangulo")
opc=int(input("Que desea hacer? 1-Crear linea con puntos 2-Crear linea base*altura \n"))

if opc==1:
    x=float(input("Valor de x --> "))
    y=float(input("Valor de y --> "))
    punto_a=Vertice(x, y)
    x=float(input("Valor de x --> "))
    y=float(input("Valor de y --> "))
    punto_b=Vertice(x, y)
    x=float(input("Valor de x --> "))
    y=float(input("Valor de y --> "))
    punto_c=Vertice(x, y)
    x=float(input("Valor de x --> "))
    y=float(input("Valor de y --> "))
    punto_d=Vertice(x, y)
    rec=Rectangulo(punto_a, punto_b, punto_c, punto_d)
elif opc==2: 
    b=float(input("Valor de base --> "))
    h=float(input("Valor de altura --> "))
    rec=Rectangulo.bh(b, h)
else:
    print("No reconocido")

while(True):
    print("Que desea hacer \n1-Mover a la Derecha \n2-Mover a la Izquierda \n3-Mover Arriba \n4-Mover abajo \n5-Ver punto \n6-Superficie \n7-Salir")
    opc=int(input())
    if opc==1:
        mov=float(input("Movimiento--> "))
        rec.mueveDerecha(mov)
    elif opc==2:
        mov=float(input("Movimiento--> "))
        rec.mueveIzquierda(mov)
    elif opc==3:
        mov=float(input("Movimiento--> "))
        rec.mueveArriba(mov)
    elif opc==4:
        mov=float(input("Movimiento--> "))
        rec.mueveAbajo(mov)
    elif opc==5:
        rec.mostrarPuntos()
    elif opc==6:
        print("Superficie es igual a --> ", rec.calcular_superficie())
    elif opc==7:
        break
    else:
        print("No reconocido")