feira = []


while True:
    itens = input('Digite os itens para fazer a feira: ')
    if itens == 'sair':
        break
        #Serve para adicionar itens
        feira.append(itens)
        #'len' serve para contar a quantidade de itens
        print(feira)
    print('Quantidade de itens adicionadas a feira:', len(feira))
