print("===============================================")
print("Sistema de verificação de matrícula de alunos")
idade = int(input("Digite a idade do aluno: "))
media = float(input("Digite a média do aluno: "))
perdefreq = float(input("Digite o percentual de frequência do aluno: "))
print("===============================================")
opc = int(input("Qual o tipo de curso do aluno? \n 1 - Graduacao \n 2 - Tecnico \n 3 - Pos-Graduacao \n Digite a opção desejada: "))
match opc:
    case 1:
        if media >= 7 and perdefreq >= 75:
            print("Aprovado")
        elif media >= 5 and perdefreq >= 75:
            print("Aprovado com restrições")
        else:
            print("Reprovado")
    case 2:
        if media >= 6 and perdefreq >= 75:
            print("Aprovado")
        elif media >= 4 and perdefreq >= 75:
            print("Recuperação")
        else:
            print("Reprovado")
    case 3:
        if media >= 7 and perdefreq >= 75:
            print("Aprovado")
        else:
            print("Reprovado")