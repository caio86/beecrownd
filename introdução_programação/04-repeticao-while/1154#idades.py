soma = 0
qtdPessoas = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    qtdPessoas += 1

media = soma / qtdPessoas

print("{:.2f}".format(media))
