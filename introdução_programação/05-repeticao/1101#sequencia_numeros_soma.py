while True:
    num1, num2 = sorted([int(x) for x in input().split()])

    if num1 <= 0 or num2 <= 0:
        break

    soma = 0

    for valor in range(num1, num2 + 1):
        soma += valor
        print(valor, end=" ")
    print(f"Sum={soma}")
