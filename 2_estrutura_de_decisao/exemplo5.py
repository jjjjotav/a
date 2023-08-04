nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:    
    if  media >= 9 and media <= 10:
        print(f'Você foi aprovado! Sua média é {media} e Você tirou A')
    elif media >= 7.5 and media < 9:
        print(f'Você foi aprovado! Sua média é {media} e Você tirou B')
    elif media >= 6 and media < 7.5:
            print(f'Você foi aprovado! Sua média é {media} e Você tirou C')
    elif media >= 4 and media < 6:
        print(f'Você foi reprovado! Sua média é {media} e Você tirou D')
    elif media > 0 and media < 4:
        print(f'Você foi reprovado! Sua média é {media} e Você tirou E')
else:
    print('ERROR!!')
