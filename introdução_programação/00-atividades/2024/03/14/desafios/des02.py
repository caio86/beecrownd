valores = input("Digite tres numeros: ").split()

n1, n2, n3 = sorted([int(x) for x in valores], reverse=True)

if n1 >= (n2 + n3):
    print("NAO")
else:
    print("SIM")

