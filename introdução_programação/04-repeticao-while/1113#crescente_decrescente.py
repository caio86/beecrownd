while True:
    x, y = [float(valor) for valor in input().split()]

    if x > y:
        print("Decrescente")
    if x < y:
        print("Crescente")
    if x == y:
        break
