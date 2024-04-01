soma = 0

num1 = int(input())
num2 = int(input())

contador = 1 if num1 - num2 < 0 else -1

for index, numero in enumerate(range(num1, num2, contador)):
    if index == 0:
        continue
    if numero % 2 == 1:
        soma += numero

print(soma)
