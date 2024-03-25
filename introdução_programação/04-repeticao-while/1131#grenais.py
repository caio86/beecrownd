# Definição de variáveis
resposta = 1

qtdVitoriasGremio = 0
qtdVitoriasInter = 0
qtdEmpates = 0
qtdGrenais = 0


while resposta == 1:
    gols = input().split()
    golsInter, golsGremio = int(gols[0]), int(gols[1])

    print("Novo grenal (1-sim 2-nao)")

    qtdGrenais += 1
    if golsGremio > golsInter:
        qtdVitoriasGremio += 1
    if golsGremio < golsInter:
        qtdVitoriasInter += 1
    if golsGremio == golsInter:
        qtdEmpates += 1

    resposta = int(input())

if qtdVitoriasGremio > qtdVitoriasInter:
    vencedor = "Gremio"
else:
    vencedor = "Inter"

# Print estatísticas
print(f"{qtdGrenais} grenais")
print(f"Inter:{qtdVitoriasInter}")
print(f"Gremio:{qtdVitoriasGremio}")
print(f"Empates:{qtdEmpates}")
print(f"{vencedor} venceu mais")
