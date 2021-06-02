from Punto import Punto
class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b

    @classmethod
    def pred(cls):
        punto_a=Punto(0, 0)
        punto_b=Punto(0, 0)
        return cls(punto_a, punto_b)

    def mueveDerecha(self, mov):
        self.punto_a.x=self.punto_a.x+mov
        self.punto_b.x=self.punto_b.x+mov

    def mueveIzquierda(self, mov):
        self.punto_a.x=self.punto_a.x-mov
        self.punto_b.x=self.punto_b.x-mov
        
    def mueveArriba(self, mov):
        self.punto_a.y=self.punto_a.y+mov
        self.punto_b.y=self.punto_b.y+mov

    def mueveAbajo(self, mov):
        self.punto_a.y=self.punto_a.y-mov
        self.punto_b.y=self.punto_b.y-mov

    def mostrarPuntos(self):
        print(self.punto_a, self.punto_b)

    
    