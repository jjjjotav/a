
from zLivro import livro

l1 = livro()
l1.__titulo = 'Jogos vorazes'
l1.__autor = 'Suzanne Collins'
l1.__ano = '14/09/2008'

l1.set_titulo('Jogos Vorazes')
print(l1.get_titulo())
