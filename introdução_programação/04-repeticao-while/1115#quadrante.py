while True:
    x, y = [float(valor) for valor in input().split()]

    if 0 in [x, y]:
        break
    if y > 0:
        if x > 0:
            print("primeiro")
        if x < 0:
            print("segundo")
    if y < 0:
        if x < 0:
            print("terceiro")
        if x > 0:
            print("quarto")
