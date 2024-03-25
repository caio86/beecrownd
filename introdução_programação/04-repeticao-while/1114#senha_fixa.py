SENHA_CORRETA = 2002

while True:
    senha = int(input())
    if senha == SENHA_CORRETA:
        print("Acesso Permitido")
        break
    print("Senha Invalida")
