dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

DIA_ATUAL = 11
MES_ATUAL = 3
ANO_ATUAL = 2024

if ano > ANO_ATUAL:
    print("EM DIA")
elif mes > MES_ATUAL:
    print("EM DIA")
elif dia >= DIA_ATUAL:
    print("EM DIA")
else:
    print("VENCIDO")
