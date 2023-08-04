class bola:
    cor = ''
    circunferencia = 0.0
    material = ''

    def troca_cor(self, t1):
        self.cor = t1
    
    def mostrar_cor(self, c):
        self.cor = c

class quadrado:
    tamanho_bola = 0.0

    def mudar_valor_lado(self, v):
        self.tamanho_bola = v

    def mostrar_valor_lado(self):
        return self.tamanho_bola
    
    def calc_area1(self, lado, altura):
        return altura * lado
    
class retangulo:
    base = 0.0
    altura = 0.0

    def mudar_valor_base(self, b):
        self.base = b
    
    def mostrar_valor_base(self):
        return self.base
    
    def calc_area2(self, base, altura):
        return base * altura
    
    def imprimir(self):
        print(f'Base: {self.base}')
        print(f'Altura: {self.altura}')

class pessoa: 
    nome = ''
    idade = 0
    peso = 0.0
    altura = 0.0

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer = (anos * 0,5)