salario = float(input("Qual o salário? "))

if salario < 2000:
    salario *= 1.1

print("R$ {}".format(salario))
