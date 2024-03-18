n1 = int(input())
n2 = int(input())
soma = 0

n1, n2 = sorted([n1, n2])

for x in range(n1, n2 +1):
    if x % 13 != 0:
        soma += x

print(soma)
