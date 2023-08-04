def converter_para_12h(horas, minutos):
    if horas == 0:
        horas_12h = 12
        periodo = 'A'
    elif horas < 12:
        horas_12h = horas
        periodo = 'A'
    elif horas == 12:
        horas_12h = 12
        periodo = 'P'
    else:
        horas_12h = horas - 12
        periodo = 'P'
    
    return horas_12h, minutos, periodo


def exibir_notacao_12h(horas, minutos, periodo):
    print(f"A hora convertida é: {horas}:{minutos:02d} {periodo}.")
    

while True:
    horas_24h = int(input("Digite as horas (formato 24h): "))
    minutos = int(input("Digite os minutos: "))

    horas_12h, minutos, periodo = converter_para_12h(horas_24h, minutos)
    exibir_notacao_12h(horas_12h, minutos, periodo)

    repetir = input("Deseja converter outra hora? (S/N): ")
    if repetir.lower() != 's':
        break