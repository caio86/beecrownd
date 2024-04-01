qtd_casos = int(input())

qtd_coelhos = 0
qtd_sapos = 0
qtd_ratos = 0
total_cobaias = 0

for caso in range(1, qtd_casos + 1):
    qtd_cobaias, tipo_cobaia = input().split()
    qtd_cobaias = int(qtd_cobaias)

    # Coelhos
    if tipo_cobaia.upper() == "C":
        qtd_coelhos += qtd_cobaias

    # Sapos
    if tipo_cobaia.upper() == "S":
        qtd_sapos += qtd_cobaias

    # Ratos
    if tipo_cobaia.upper() == "R":
        qtd_ratos += qtd_cobaias

    total_cobaias += qtd_cobaias

percentual_coelhos = qtd_coelhos / total_cobaias * 100
percentual_ratos = qtd_ratos / total_cobaias * 100
percentual_sapos = qtd_sapos / total_cobaias * 100

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {qtd_coelhos}")
print(f"Total de ratos: {qtd_ratos}")
print(f"Total de sapos: {qtd_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
