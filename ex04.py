idade = int(input("Digite sua idade: "))
sal = float(input("Digite seu salário: R$"))
tdt = float(input("Digite o tempo de trabalho em anos: "))
vals = float(input("Digite o valor solicitado: R$"))
erros = []

if idade < 18:
    erros.append("Idade insuficiente.")

if sal < 1500:
    erros.append("Salário insuficiente.")

if tdt < 1:
    erros.append("Tempo de trabalho insuficiente.")

if vals > (sal * 10):
    erros.append("Valor solicitado maior que o permitido.")

if len(erros) == 0:
    print("Empréstimo pre-aprovado!")
else:
    print("Empréstimo negado devido aos seguintes motivos:")
    for erro in erros:
        print("- " + erro)