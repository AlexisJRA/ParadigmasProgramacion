from Obrero import Obrero
from Administrador import Administrador
from Intendente import Intendente
from Empleado import Empleado

obreros=[]
administradores=[]
intendentes=[]
opc="S"


print("Empresa Patito")

while opc=="S":

    te=int(input("¿Que deseas añadir?  --- 1-Obrero --- 2-Administrador --- 3-Intendente \n"))

    if te==1:
        id=int(input("Ingrese ID de obrero ---> "))
        nombre=input("Ingrese nombre ---> ")
        sueldo=int(input("Ingrese sueldo ---> "))
        asistencia=int(input("Ingrese días trabjados --> "))
        obrero_aux=Obrero(id, nombre, sueldo, asistencia)
        obreros.append(obrero_aux)
        print("Obrero añadido")

    elif te==2:
        id=int(input("Ingrese ID --> "))
        nombre=input("Ingrese nombre --> ")
        sueldo=int(input("Ingrese sueldo --> "))
        ventas=int(input("Ingrese monto de venta --> "))
        administrador_aux=Administrador(id, nombre, sueldo, ventas)
        administradores.append(administrador_aux)
        print("Administrador añadido")
        
    else:
        id=int(input("Ingrese ID --> "))
        nombre=input("Ingrese nombre --> ")
        sueldo=int(input("Ingrese sueldo --> "))
        turnos=int(input("Ingrese turnos trabjados --> "))
        intendente_aux=Intendente(id, nombre, sueldo, turnos)
        intendentes.append(intendente_aux)
        print("Intendente añadido")
    
    opc=input("¿Quiere seguir capturando? S/N \n")

suma_so=0
suma_sa=0
suma_si=0

for obrero in obreros:
    obrero.c_asistencia()
    suma_so+=obrero.sueldof

for administrador in administradores:
    administrador.bono_mensual()
    suma_sa=+administrador.sueldof

for intendente in intendentes:
    intendente.c_turnos()
    suma_si=+intendente.sueldof

print("Salario total de obreros-->", suma_so, "\nSalario total de administradores--> ", suma_sa,"\nSalario total de intendentes-->", suma_si)


