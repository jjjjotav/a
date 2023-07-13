
numero1 = 8
numero2 = 10
numero3 = 5
# se numero1 for maior que numero 2 ele faz a troca
if numero1 > numero2:
    auxiliar = numero1
    numero1 = numero2
    numero2 = auxiliar
# se numero2 for maior que numero3 ele faz a troca
if numero2 > numero3:
    auxiliar = numero2
    numero2 = numero3
    numero3 = auxiliar
# se numero1 for maior que numero2 ele faz a troca
if numero1 > numero2:
    auxiliar = numero1
    numero1 = numero2
    numero2 = auxiliar

    print(f" {numero1} <= {numero2} <= {numero3}")