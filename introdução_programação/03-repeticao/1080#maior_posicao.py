maiorNumero = 0
maiorPosicao = 0
for posicao in range(1, 100 +1):
    num = int(input())
    if num > maiorNumero:
        maiorNumero = num
        maiorPosicao = posicao

print(maiorNumero)
print(maiorPosicao)
