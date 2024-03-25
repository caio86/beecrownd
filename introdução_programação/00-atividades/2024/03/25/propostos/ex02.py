maior = float("-inf")
menor = float("inf")

while True:
    nota = int(input("Nota: "))
    if nota not in range(1, 100 + 1):
        break

    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

print("-=" * 6)
print(f"Menor: {menor}")
print(f"Maior: {maior}")
