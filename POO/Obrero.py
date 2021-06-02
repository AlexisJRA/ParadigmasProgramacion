from Empleado import Empleado

class Obrero(Empleado):

    def __init__(self, id, nombre, sueldo, asistencia):
        Empleado.__init__(self, id, nombre, sueldo)
        self.asistencia=asistencia
        self.sueldof=sueldo

    def c_asistencia(self):
        if 30>self.asistencia:
            print("Obrero: " , self.nombre, " tendrá descuento")
            self.descuento()
        else:
            print("Obrero: " ,self.nombre, " tendrá bono")
            self.bono()

    def descuento(self):
        self.sueldof= 30-self.asistencia*self.sueldo/30
            
    def bono(self):
        self.sueldof=self.sueldo*1.1
