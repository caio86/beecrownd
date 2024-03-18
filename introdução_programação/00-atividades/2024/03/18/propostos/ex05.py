qtd_sim = 0
qtd_nao = 0

qtd_votos = 80

for x in range(1, qtd_votos + 1):
    voto = input("Qual o seu voto? [SIM/NAO] ")
    if voto == "SIM":
        qtd_sim += 1
    else:
        qtd_nao += 1

porcentagem_sim = (qtd_sim / qtd_votos) * 100
porcentagem_nao = (qtd_nao / qtd_votos) * 100

print("-="*16)
print(f"Porcetagem da votação:")
print(f"SIM: {porcentagem_sim:.0f}%")
print(f"NAO: {porcentagem_nao:.0f}%")
