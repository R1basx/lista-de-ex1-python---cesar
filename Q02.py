# Classificação de produto
preco = float(input("Digite o preço do produto: R$"))
estoque = int(input("Quantidade em estoque: "))

if preco <= 0:
    print("preço invalido.")
elif estoque <= 0:
    print("Quantidade invalida.")
elif preco <= 0 and estoque <=0:
    print("Preço e quantidade invalidos.")
elif preco > 1000 and estoque < 5:
    print("Produto caro com estoque crítico.")
elif preco > 1000 and estoque < 21:
    print("Produto caro com estoque normal.")
elif preco > 1000 and estoque > 20:
    print("Produto caro com estoque alto.")
elif preco < 1000 and estoque < 5:
    print("Estoque crítico.")
else:
    print("Estoque normal.")