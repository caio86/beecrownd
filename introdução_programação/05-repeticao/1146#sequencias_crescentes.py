while True:
    numero = int(input())

    if numero == 0:
        break

    for x in range(1, numero + 1):
        if x == numero:
            espacamento = "\n"
        else:
            espacamento = " "

        print(f"{x}", end=espacamento)
