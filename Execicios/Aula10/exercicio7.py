resposta = "S"
while resposta == "S":
    base = int(input("Escolha a base: "))
    expoente = int(input("Escolha o expoente: "))
    print(str(base) + " ** " + str(expoente) + " = " + str(base**expoente))
    resposta = input("Deseja continuar? S/N ").upper()
print("Obrigado por usar o nosso sistema!")