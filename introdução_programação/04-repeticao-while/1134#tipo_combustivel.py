valor = 0

qtdAlcool = 0
qtdGasolina = 0
qtdDeisel = 0

while valor != 4:
    valor = int(input())

    if valor == 1:
        qtdAlcool += 1
    elif valor == 2:
        qtdGasolina += 1
    elif valor == 3:
        qtdDeisel += 1

print("MUITO OBRIGADO")
print(f"Alcool: {qtdAlcool}")
print(f"Gasolina: {qtdGasolina}")
print(f"Diesel: {qtdDeisel}")
