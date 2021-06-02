from Empleado import Empleado

class Intendente(Empleado):

    def __init__(self, id, nombre, sueldo, turnos):
        Empleado.__init__(self, id, nombre, sueldo)
        self.turnos=turnos
        self.sueldof=sueldo

    def c_turnos(self):
        if 30>self.turnos:
            print("Intendente: ", self.nombre, " tendrá descuento")
            self.descuento()
        else:
            print("Intendente: ", self.nombre, " tendrá bono")
            self.bono()

    def descuento(self):
        self.sueldof= 30-self.turnos*self.sueldo/30
            
    def bono(self):
        self.sueldof=self.sueldo*1.1
