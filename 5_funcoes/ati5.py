def somaImposto(taxaImposto, custo):
    imposto = custo * taxaImposto / 100
    custo = custo + imposto
    return custo

taxaImposto = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo: "))
custo = somaImposto(taxaImposto, custo)
print(f"O custo com o imposto é de R${custo:.2f}")
