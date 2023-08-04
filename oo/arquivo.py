class pessoa:
   
    peso = 0.0
    altura = 0.0

    def __init__(self, n, snome): 
        self.nome = n
        self.sobrenome = snome



    def andar(self):
        print('pessoa está andando')

    def falar(self):
        print('pessoa está falando...')
    
    def calcIMC(self, altura, peso):
        return peso / altura ** 2
    
    def alterar_peso(self, p):
        self.peso = p

    def pegar_peso(self):
        return self.peso

    def imprimir(self):
        print(f'Nome: {self.nome} ')
        print(f'Sobrenome: {self.sobrenome}')
        print(f'peso: {self.peso}')
        print(f'Altura: {self.altura}')

    def __str__(self):
        return f'Nome: {self.nome} \nSobrenome: {self.sobrenome} \nPeso: {self.peso} \nAltura: {self.altura}'

'''if __name__ == '__main__':
p1 = pessoa()   
p1.nome = 'Maria' 
p1.sobrenome = 'Silva'
p1.peso = 50.20
p1.altura = 180.00

print(f'Nome: {p1.nome} ')
print(f'Sobrenome: {p1.sobrenome}')
print(f'peso: {p1.peso}')
print(f'Altura: {p1.altura}')


p1.alterar_peso(60.7)
p1.pegar_peso()
p1.falar()
p1.andar()
print(f'IMC: {p1.calcIMC(p1.peso, p1.altura)}')
p1.imprimir()'''