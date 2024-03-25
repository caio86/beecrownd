soma = 0
while True:
    numero = int(input("Número: "))
    soma += numero
    if soma > 100:
        break

print(f"Soma = {soma}")
