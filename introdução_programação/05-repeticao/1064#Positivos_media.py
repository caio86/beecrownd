valores_positivos = 0
qtd_valores = 0
soma = 0

for _ in range(0, 6):
    valor = float(input())

    if valor > 0:
        valores_positivos += 1
        soma += valor
        qtd_valores += 1

qtd_valores = 1 if qtd_valores == 0 else qtd_valores
media = soma / qtd_valores

print(f"{valores_positivos} valores positivos")
print(f"{media:.1f}")
