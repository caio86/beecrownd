META = 1000

arrecadado = 0
qtdDoacoes = 0

while True:
    valor = float(input("Qual a sua doação? "))
    if valor > 0:
        qtdDoacoes += 1
        arrecadado += valor
    if arrecadado >= META:
        break

valorExtra = arrecadado - META

print(f"Arrecadação: R$ {arrecadado:.2f}")
print(f"Quantidade de doações: {qtdDoacoes}")
print(f"Valor extra arrecadado: {valorExtra:.2f}")
