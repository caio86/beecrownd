idade = int(input("Qual a sua idade? "))

if idade < 16:
    print("Não pode votar")
elif idade < 18:
    print("Voto opcional")
elif idade <= 70:
    print("Voto obrigatório")
else:
    print("Voto opcional")
