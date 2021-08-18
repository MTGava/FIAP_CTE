valorEscolhido = int(input("Deseja calcular a tabuada de qual número? "))

for contador in range(0, 11, 1):
    print(str(valorEscolhido) + " x " + str(contador) + " = " + str(valorEscolhido*contador))

