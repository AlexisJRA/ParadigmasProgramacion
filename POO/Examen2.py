from Linea import Linea
from Punto import Punto

print("Programa que crea línea")
opc=int(input("Que desea hacer? 1-Crear linea x,y 2-Crear linea 0,0 \n"))

if opc==1:
    x=float(input("Valor de x --> "))
    y=float(input("Valor de y --> "))
    punto_a=Punto(x, y)
    x=float(input("Valor de x --> "))
    y=float(input("Valor de y --> "))
    punto_b=Punto(x, y)
    linea=Linea(punto_a, punto_b)
elif opc==2:
    linea=Linea.pred()
else:
    print("No reconocido")

while(True):
    print("Que desea hacer \n1-Mover a la Derecha \n2-Mover a la Izquierda \n3-Mover Arriba \n4-Mover abajo \n5-Ver punto \n6-Salir")
    opc=int(input())
    if opc==1:
        mov=float(input("Movimiento--> "))
        linea.mueveDerecha(mov)
    elif opc==2:
        mov=float(input("Movimiento--> "))
        linea.mueveIzquierda(mov)
    elif opc==3:
        mov=float(input("Movimiento--> "))
        linea.mueveArriba(mov)
    elif opc==4:
        mov=float(input("Movimiento--> "))
        linea.mueveAbajo(mov)
    elif opc==5:
        linea.mostrarPuntos()
    elif opc==6:
        break
    else:
        print("No reconocido")