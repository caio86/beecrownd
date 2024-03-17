qt_positivo = 0
qt_negativo = 0
qt_zero = 0

for i in range(10):
    num = int(input("numero: "))
    if (num > 0):
        qt_positivo = qt_positivo + 1
    else:
        if (num < 0):
            qt_negativo = qt_negativo + 1
        else:
            qt_zero = qt_zero + 1

print("Positivos:", qt_positivo)
print("Negativos:", qt_negativo)
print("Zeros:", qt_zero)
