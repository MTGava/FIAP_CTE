numeroEscolhido = int(input("Digite o número que você deseja fatorar: "))
resultado = numeroEscolhido
if numeroEscolhido>0:
    while numeroEscolhido>1:
        numeroEscolhido-=1
        resultado = resultado * numeroEscolhido
    print(resultado)
elif numeroEscolhido == 0:
    print(1)
else:
    print("Valor menor que zero")