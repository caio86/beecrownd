qtd_repeticoes = int(input())

for _ in range(qtd_repeticoes):
    x, y = [int(valor) for valor in input().split()]

    if y == 0:
        print("divisao impossivel")
        continue

    divisao = x / y
    print("{:.1f}".format(divisao))
