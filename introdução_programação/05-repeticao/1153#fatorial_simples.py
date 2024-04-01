numero = int(input())

fatorial = 1

for valor in range(numero, 0, -1):
    fatorial = fatorial * valor

print(fatorial)
