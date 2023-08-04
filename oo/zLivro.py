from datetime import date
class livro:
    __titulo = ''
    __autor = ''
    __ano = ''

    @property
    def get_titulo(self):
        return self.__titulo

    @get_titulo.setter    
    def set_titulo(self, novo_titulo):
         self.__titulo = novo_titulo

    def imprimir(self):
        print(f'Titulo: {self.__titulo}')
        print(f'Autor: {self.__autor}')
        print(f'Ano da publicação: {self.__ano}')

    