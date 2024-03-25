soma = 0
qtd = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    qtd += 1
    soma += numero

if qtd == 0:
    qtd = 1
media = soma / qtd

print(f"Média: {media}")
