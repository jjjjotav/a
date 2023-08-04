from math import pi
from forma import forma
class circulo(forma):
    def __init__(self):
        super().__init__()
        self.raio = 0.0

    def AreaCirculo(self):
        return (self.raio * self.raio) * pi 
    
    def __str__(self):
        return f'Raio: {self.raio}'