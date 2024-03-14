valor = float(input("Qual o valor da compra? "))

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

cashback = valor * (aliquota / 100)

print(f"Alíquota: {aliquota}%")
print(f"R$ {cashback:.2f} de Cashback")
