from brinquedo import Brinquedo

class Car(Brinquedo):

    def __init__(self):
        self.marca = str
        self.controle =  bool 

    def __str__(self):
        return f'Marca: {self.marca}\nPossue controle remoto: {self.controle}'
