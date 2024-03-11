valores = input("Digite tres valores: ").split()

n1, n2, n3 = [int(x) for x in valores]

aritmetica = (n1 + n2 + n3) / 3
ponderada = (n1 * 2 + n2 * 6 + n3 * 4) / (2 + 6 + 4)

print(f"PONDERADA: {ponderada}")
print(f"ARITMETICA: {aritmetica}")
print()

if ponderada > aritmetica:
    print("PONDERADA")
elif aritmetica > ponderada:
    print("ARITMETICA")
elif ponderada == aritmetica:
    print("TANTO FAZ")

