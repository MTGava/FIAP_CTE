nota1Aluno = int(input("Digite a sua primeira nota: "))
nota2Aluno = int(input("Digite a sua segunda nota: "))
nota3Aluno = int(input("Digite a sua terceira nota: "))
nota4Aluno = int(input("Digite a sua quarta nota: "))
mediaAluno = (nota1Aluno + nota2Aluno + nota3Aluno + nota4Aluno) / 4
mediaEscola = 7

if mediaAluno >= mediaEscola:
    print("Aprovado! Parabéns")
elif mediaAluno < mediaEscola and mediaAluno > 3:
    print("Aluno está de exame")
else:
    print("Reprovado! Tente novamente")
print("Sua média foi", mediaAluno)