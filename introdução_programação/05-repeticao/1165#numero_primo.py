qtd_casos = int(input())

for _ in range(qtd_casos):
    numero = int(input())
    divisiveis = 0
    for valor in range(numero, 0, -1):
        if numero % valor == 0:
            divisiveis += 1
    if divisiveis == 2:
        print(f"{numero} eh primo")
    else:
        print(f"{numero} nao eh primo")
