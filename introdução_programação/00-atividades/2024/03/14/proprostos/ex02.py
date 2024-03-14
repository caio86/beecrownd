nome1 = input("Nome da primeira pessoa: ")
idade1 = int(input(f"Qual a idade de {nome1}: "))
nome2 = input("Nome da segunda pessoa: ")
idade2 = int(input(f"Qual a idade de {nome2}: "))

if idade1 >= idade2:
    print(nome1)
else:
    print(nome2)
