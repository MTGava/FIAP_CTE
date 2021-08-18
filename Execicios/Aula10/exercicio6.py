numeroEscolhido = int(input("Digite até qual posição você deseja ver na sequência de Fibonacci: "))
if numeroEscolhido > 0:
    numeroAtual = 1
    numeroAnterior = 0
    print("============================")
    for contador in range(0, numeroEscolhido, 1):
        print(numeroAtual)
        numeroPosterior = numeroAnterior + numeroAtual
        numeroAnterior = numeroAtual
        numeroAtual = numeroPosterior
    print("============================")
    print("Sequência de Fibonacci finalizada.")
