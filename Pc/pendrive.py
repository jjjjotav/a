from computador import armazenamento

class pendrive(armazenamento):
    
    def __init__(self, tipo, capacidade, marca):
        super().__init__(tipo, capacidade)
        self.marca = marca

    def __str__(self):
        return f'Tipo: {self.tipo}\nCapacidade: {self.capacidade}\nMarca: {self.marca}'
    
pendrive = pendrive ('Flash', '1TB', 'Sandisk')

print(pendrive)


pendrive.funcionr()
 