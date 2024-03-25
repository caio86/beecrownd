import random

valor_aleatorio = random.randint(1, 100)
erros = 0

# print(valor_aleatorio)  # Pra facilitar os testes

print("Tente acerta o número: [1-100]")

while True:
    chute = int(input("Digite o seu chute: "))
    if chute == valor_aleatorio:
        break
    erros += 1

print("Acertou!")
print(f"Errou {erros} vezes!")
