numeroInicial = int(input("Digite o número inicial: "))
numeroFinal = int(input("Digite o número fimal: "))

for contador in range(numeroInicial, numeroFinal+1, 1):
    print(str(contador) + "²" + " = " + str(contador**2))
