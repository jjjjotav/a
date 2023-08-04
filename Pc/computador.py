class memoria:
    def __init__(self, marca, capacidade):
        self.marca = marca
        self.capacidade = capacidade


    def __str__(self):
        return f'{self.marca} - {self.capacidade}'

class processador:

    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

    def __str__(self):
        return f'{self.modelo} - {self.velocidade}'
    
class armazenamento:
    
    def __init__(self, tipo, capacidade):
        self.tipo = tipo
        self.capacidade = capacidade

    def __str__(self):
        return f'{self.tipo} - {self.capacidade}'
    
    def funcionr(self):
        print('O armazenamento está funcionando: ')

class computador:
    def __init__(self, memoria, armazenamento, processador):
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.processador = processador

    def __str__(self):
        return f'memoria: {self.memoria} \narmazenamento: {self.armazenamento} \nprocessador: {self.processador}'
    

Memoria = memoria('kingston', '16gb/RAM')
Processador = processador('Ryzen 9','3.9 Mg/hz')
Armazenamento = armazenamento('Ssd','1TB')

Computador = computador(Memoria, Armazenamento, Processador)
print(Computador)
    


