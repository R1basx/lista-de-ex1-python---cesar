print("===============================")
print("   1 - cadastrar novo aluno    ")
print("   2 - consultar aluno         ")
print("   3 - alterar aluno           ")
print("   4 - excluir aluno           ")
print("   5 - listar alunos           ")
print("   6 - sair                    ")
print("===============================")

opc = int(input("Digite a opção desejada: "))
match opc:
    case 1:
        print("Cadastrar novo aluno")
    case 2:
        print("Consultar aluno")
    case 3:
        print("Alterar aluno")
    case 4:
        print("Excluir aluno")
    case 5:
        print("Listar alunos")
    case 6:
        print("Sair")
if opc < 1 or opc > 6:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")