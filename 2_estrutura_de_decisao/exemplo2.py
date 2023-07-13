n1 = float (input("Digite o primeiro numero: "))
n2 = float (input("Digite o segundo numero: "))
n3 = float (input("Digite o terceiro numero: "))

primeiro = n1 > n2 and n1 > n3
segundo = n2 > n1 and n2 > n3

if primeiro:
    print("O primeiro numero é maior: ")
elif segundo:
    print("O segundo numero é o maior: ")
else:
    print("O terceiro é o maior: ")