qtd_piramides = 0

for x in range(1, 7):
    lados = input(f"Quais os lados do {x}ª triângulo: ").split()

    # converte e ordena os valores
    lados = [float(valor) for valor in lados]
    lado1, lado2, lado3 = sorted(lados, reverse=True)

    if lado1 < lado2 + lado3:
        qtd_piramides += 1

print(f"Quantidade de pirâmides: {qtd_piramides}")
