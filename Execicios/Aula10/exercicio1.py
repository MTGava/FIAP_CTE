salarioUsuario = float(input("Digite o seu salário: "))
valorPrestacao = float(input("Digite o valor da prestação: "))
credito = salarioUsuario * 0.30
if valorPrestacao < credito:
    print("Crédito concedido")
else:
    print("Crédito NÃO concedido")
