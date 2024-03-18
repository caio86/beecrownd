pares_crescentes = 0

for i in range(8):
  num1, num2 = input("Informe dois números: ").split()
  num1, num2 = int(num1), int(num2)
  if (num1 < num2):
    pares_crescentes = pares_crescentes + 1

print('Quantidade de pares crescentes:', pares_crescentes)
