class Brinquedo:
    def __init__(self):
        self.tipo = str
        self.faixaE = str
        self.preco = 0.0

    def ligar(self):
        print('O brinquedo está ligado.')

    def desligar(self):
        print('O bronquedo está desligado.')

    def imprimir(self):
        print(f'Tipo: {self.tipo}\nFaixa: {self.faixaE}\nPreco: {self.preco}\n')

