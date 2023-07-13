resposta = "nao"
contador = 1

while resposta != "sim":
        resposta = input(f"Tentativa: {contador} | Eu sou bonito?")
        #contador = contador + 1
        contador += 1
       #para limitar o contador usar para limitar: if contador == 10: break
        print("Obrigado por responder! ")


