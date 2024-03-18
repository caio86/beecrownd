soma = 0

for x in range(1, 7):
    soma += float(input(f"Digite a {x}ª nota: "))

media = soma/6

print(f"Média = {media:.2f}")
