# Separa as variáveis em uma array
coordenadas = input().split()

# Converte as variáveis em float
x, y = [float(x) for x in coordenadas]

if y > 0:
    if x > 0:
        print("Q1")
    elif x < 0:
        print("Q2")
    else:
        print("Eixo Y")
elif y < 0:
    if x > 0:
        print("Q4")
    elif x < 0:
        print("Q3")
    else:
        print("Eixo Y")
elif y == 0:
    if x != 0:
        print("Eixo X")
    else:
        print("Origem")
