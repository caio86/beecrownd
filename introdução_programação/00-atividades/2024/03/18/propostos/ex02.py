qtd_valida = 0

for x in range(1, 9):
    nota = int(input(f"Digite a nota do {x}ª: "))
    if nota in range(0, 101):
        qtd_valida += 1

print(f"Foram informadas {qtd_valida} notas válidas para o suap")
