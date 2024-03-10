valores = input().split()

lados = [float(x) for x in valores]
lados.sort(reverse = True)

CONDICAO_ISOSCELES=lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]

if lados[0] >= (lados[1] + lados[2]):
    print("NAO FORMA TRIANGULO")
else:
    if lados[0]**2 == (lados[1]**2 + lados[2]**2):
        print("TRIANGULO RETANGULO")
    elif lados[0]**2 > (lados[1]**2 + lados[2]**2):
        print("TRIANGULO OBTUSANGULO")
    elif lados[0]**2 < (lados[1]**2 + lados[2]**2):
        print("TRIANGULO ACUTANGULO")
    if lados[0] == lados[1] == lados[2]:
        print("TRIANGULO EQUILATERO")
    elif CONDICAO_ISOSCELES:
        print("TRIANGULO ISOSCELES")
