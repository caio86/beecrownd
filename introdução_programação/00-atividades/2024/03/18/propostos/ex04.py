valor_total = 0
cashback_total = 0

for compra in range(1, 401):
    valor = float(input(f"Valor da compra n.{compra}º: "))
    
    if valor <= 100:
        # Até 100
        aliquota = 4
    elif valor <= 200:
        # entre 100,01 e 200
        aliquota = 6
    elif valor <= 400:
        # entre 201,01 e 400
        aliquota = 8
    else:
        # acima de 400
        aliquota = 10

    valor_total += valor
    cashback_total += valor * (aliquota / 100)

print(f"Valor total: R${valor_total:.2f}")
print(f"Cashback total: R${cashback_total:.2f}")
