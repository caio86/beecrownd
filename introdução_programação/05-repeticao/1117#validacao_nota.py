soma = 0

for _ in range(2):
    while True:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            soma += nota
            break
        print("nota invalida")

media = soma / 2
print(f"media = {media:.2f}")
