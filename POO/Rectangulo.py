from Vertice import Vertice
class Rectangulo:
    def __init__(self, punto_a, punto_b, punto_c, punto_d):
        self.punto_a=punto_a
        self.punto_b=punto_b
        self.punto_c=punto_c
        self.punto_d=punto_d
        self.base=abs(punto_a.x-punto_b.x)
        self.altura=abs(punto_a.y-punto_c.y)
    
    @classmethod
    def bh(cls, base, altura):
        punto_a=Vertice(0, 0)
        punto_b=Vertice(base, 0)
        punto_c=Vertice(0, altura)
        punto_d=Vertice(altura, base)
        return cls(punto_a, punto_b, punto_c, punto_d)

    def calcular_superficie(self):
        return self.base*self.altura

    def mueveDerecha(self, mov):
        self.punto_a.x=self.punto_a.x+mov
        self.punto_b.x=self.punto_b.x+mov
        self.punto_c.x=self.punto_c.x+mov
        self.punto_d.x=self.punto_d.x+mov
        
    def mueveIzquierda(self, mov):
        self.punto_a.x=self.punto_a.x-mov
        self.punto_b.x=self.punto_b.x-mov
        self.punto_c.x=self.punto_c.x-mov
        self.punto_d.x=self.punto_d.x-mov

    def mueveArriba(self, mov):
        self.punto_a.y=self.punto_a.y+mov
        self.punto_b.y=self.punto_b.y+mov
        self.punto_c.y=self.punto_c.y+mov
        self.punto_d.y=self.punto_d.y+mov

    def mueveAbajo(self, mov):
        self.punto_a.y=self.punto_a.y-mov
        self.punto_b.y=self.punto_b.y-mov
        self.punto_c.y=self.punto_c.y-mov
        self.punto_d.y=self.punto_d.y-mov

    def mostrarPuntos(self):
        print(self.punto_c, self.punto_d, "\n", self.punto_a, self.punto_b)