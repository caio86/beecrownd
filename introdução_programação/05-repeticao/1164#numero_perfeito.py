qtd_casos = int(input())

for _ in range(qtd_casos):
    numero = int(input())

    soma_divisores = 0

    for valor in range(1, numero):
        if numero % valor == 0:
            soma_divisores += valor

    if soma_divisores == numero:
        print(f"{numero} eh perfeito")
    else:
        print(f"{numero} nao eh perfeito")
