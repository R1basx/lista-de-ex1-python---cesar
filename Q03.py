# Elegibilidade para bolsa
Macad = float(input("Digite a média acadêmica do estudante: "))
Pfreq = float(input("Digite o percentual de frequência do estudante: ""%"))
Rfamil = float(input("Digite a renda familiar do estudante: R$"))
OutraB = str(input("Estudante possui outra bolsa? [S/N] ")).strip().upper()

erros = []

if Macad < 7:
    erros.append("Motivo: Media academica insuficiente.")

if Pfreq < 75:
    erros.append("Motivo: percentual de frequencia insuficiente.")

if Rfamil > 3000:
    erros.append("Motivo: Renda acima do limite.")

if OutraB == "S":
    erros.append("Motivo: Estudante já possui outra bolsa ativa.")

if len(erros) == 0:
    print("\nAluno elegivel para bolsa!")
else:
    print("\nAluno NAO elegivel para bolsa!")
    for erro in erros:
        print(erro)