class animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print('Animal falando...')

    def imprimir(self):
        print(f'Nome: {self.nome}')


class mamifero(animal):
    
    def __init__(self, nome, corpelo):
        super().__init__(nome)
        self.corpelo = corpelo

    def imprimir(self):
        super().imprimir()
        print(f'Cor: {self.corpelo}')

class voador(animal):
    def __init__(self, nome, envergadura):
        # super().__init__(nome)
        self.envergadura = envergadura

    def imprimir(self):
        # super().imprimir()
        print(f'Envergadura: {self.envergadura}')



mamifero1 = mamifero('Cachorro', 'Preto')
mamifero1.falar()
mamifero1.imprimir()

print('-' * 20)
animal1 = animal('Gato')
animal1.imprimir()

print('-' * 20)
voador1 = voador('Passaro', True)
voador1.imprimir()

class cachorro(mamifero):
    def __init__(self, nome, corpelo, raca):
        super().__init__(nome, corpelo)
        self.raca = raca

    def imprimir(self):
        print(f'Raça: {self.raca}')

    def falar(self):
        print(f'O cachorro está falando...')



class gato(mamifero): 
    def __init__(self, nome, corpelo, caudapompom):
        super().__init__(nome, corpelo)
        self.caudapompom = caudapompom

    def imprimir(self):
        print(f'Cauda Pompom: {self.caudapompom}')

    def falar(self):
        print('O gato está miando...')


class passaro(voador):
    def __init__(self, nome, envergadura, corpenas):
        super().__init__(nome, envergadura)
        self.corpenas = corpenas

    def imprimir(self):
        print(f'Cor da pena: {self.corpenas}')

    def falar(self):
        print('O passaro está cantando...')