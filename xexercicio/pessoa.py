class pessoa:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}\nCpf: {self.cpf}\nSálario: {self.salario}')

class funcionario(pessoa):
    def __init__(self, nome, cpf, cargo, horas, salario):
        super().__init__(nome, cpf)
        self.horas = horas
        self.salario = salario
        self.cargo = cargo

    def informacoes_funcionario(self):
        super().mostrar_informacoes()
        print(f'Cargo: {self.cargo}')


    def calculo_horaExtra(self):
        print(f'Valor da hora extra: {self.horas * 15}\nSalário + hora extra: {self.salario + (self.horas * 15)}')
        
    

class gerente(pessoa):
    def __init__(self, nome, cpf, setor, quantidade_equipe, salario):
        super().__init__(nome, cpf, salario)
        self.quantidade_equipe = quantidade_equipe
        self.setor = setor


    def informacoes_gerente(self):
        super().mostrar_informacoes()
        print(f'Setor: {self.setor}\nQuantidade da equipe: {self.quantidade_equipe}')

    def calculo_bonificação(self):
        if self.quantidade_equipe >= 10:
            return self.salario * 1.10
        else:
            return self.salario * 1.05

    
        
    




