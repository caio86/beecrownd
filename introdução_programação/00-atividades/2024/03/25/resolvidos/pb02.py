qtd = 0

while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    if numero > 0:
        qtd += 1

print("Quantidade de números digitados:", qtd)
