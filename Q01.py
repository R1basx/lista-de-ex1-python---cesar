# Classificação de Idade
idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade invalida.")
elif idade < 13:
    print("Você é uma criança!")
elif idade < 18:
    print("Você é um adolescente!")
elif idade < 60:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")