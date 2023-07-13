
numero1 = float (input("Digite a 1° nota: "))
numero2 = float (input("Digite a 2° nota: "))
numero3 = float (input("Digite a 3° nota: "))

media = (numero1 + numero2 + numero3) / 3
print(f"A media das três nota : {media}")

aprovado = media >=70
reprovado = media < 30

if aprovado:
    print("Parabéns, você foi aprovado ")
elif reprovado:
    print("Infelizmente você foi reprovado")
else:
    print("Você está na 4° prova ")