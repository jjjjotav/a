from brinquedo import Brinquedo
    
class boneca(Brinquedo):

    def __init__(self):
        super().__init__()
        self.tamanho = int
        self.nome = str


    def __str__(self):
        return f'Tamanho: {self.tamanho}\nNome: {self.nome}'