numeroEscolhido = int(input("Digite o número para ser somado: "))
resultado = numeroEscolhido
if numeroEscolhido >= 0:
    while numeroEscolhido > 0:
        numeroEscolhido-=1
        resultado = resultado + numeroEscolhido
    print(resultado)
