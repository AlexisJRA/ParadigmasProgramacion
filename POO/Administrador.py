from Empleado import Empleado
class Administrador(Empleado):

    def __init__(self, id, nombre, sueldo, ventas):
        Empleado.__init__(self, id, nombre, sueldo)
        self.ventas=ventas
        self.sueldof=sueldo

    def bono_mensual(self):
        if self.ventas>=100000:
            print("Administrador: " , self.nombre, " tiene bono")
            self.sueldof=self.sueldo*1.2
        else:
            print("Administrador: ", self.nombre, " no tiene bono")


    


