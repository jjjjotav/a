def valor(numero):
    if numero > 0:
        return "P"
    else:
        return "N"
    

resultado = (f"Resultado: {valor(1)}")
print(resultado)
resultado = (f"Resultado: {valor(-1)}")
print(resultado)