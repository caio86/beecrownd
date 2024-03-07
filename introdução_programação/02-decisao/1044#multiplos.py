valores = input().split()

n1, n2 = [int(x) for x in valores]

SAOMULTIPLOS = "Sao Multiplos"
NAOSAOMULTIPLOS = "Nao sao Multiplos"

if n1 > n2:
    if n1 % n2 == 0:
        multiplos = True
    else:
        multiplos = False
else:
    if n2 % n1 == 0:
        multiplos = True
    else:
        multiplos = False

print(SAOMULTIPLOS if multiplos else NAOSAOMULTIPLOS)
