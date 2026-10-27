ndp = int(input("Digite a nota de produtividade: "))
ndq = int(input("Digite a nota de qualidade: "))
pdf = int(input("Digite o percentual de frequencia: "))
media = (ndp + ndq) / 2

if pdf < 75:
    print("Desempenho comprometido por baixa frequência.")

if media >= 9 and pdf >= 90:
    print("Desempenho excelente!")
elif media >= 7 and pdf >= 85:
    print("Desempenho bom!")
elif media >= 5 and pdf >= 75:
    print("Desempenho regular.")
else:
    print("Desempenho insatisfatório.")