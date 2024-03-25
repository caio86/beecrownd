qtdSopa = 1000  # em ml
qtdBeneficiados = 0

while True:
    tamanhoRecipiente = int(input())
    qtdSopa -= tamanhoRecipiente
    qtdBeneficiados += 1
    if qtdSopa <= 0:
        break

print(f"Beneficiados: {qtdBeneficiados}")
if qtdSopa < 0:
    print(f"O último beneficiado foi incompleto, faltou: {abs(qtdSopa)}ml")
else:
    print("Todos satisfeitos!")
