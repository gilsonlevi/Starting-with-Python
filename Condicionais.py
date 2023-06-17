# notaAluno = int(input("Digite a nota do aluno:"))

# if notaAluno >=6:
#     print("Está na media")
# elif notaAluno < 6 and notaAluno >=4:
#     print("Está em recuperação")
# else:
#     print("Está reprovado")
notaAluno = "S"
while True:
    notaAluno = input("Digite a nota do aluno:")
    print("Digite 'F' para finalizar")
    if notaAluno == "F":
        break
    else:
        notaAluno =  int(notaAluno)
        if notaAluno >=6:
            print("Está na media")
        elif notaAluno < 6 and notaAluno >=4:
            print("Está em recuperação")
        else:
            print("Está reprovado")
