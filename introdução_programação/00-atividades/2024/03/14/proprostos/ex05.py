mes = int(input("Digite o numero do mês [1-12]: "))

MES_COM_30_DIAS = [4, 6, 9, 11]

if mes == 2:
    print("29 dias")
elif mes in MES_COM_30_DIAS:
    print("30 dias")
else:
    print("31 dias")
