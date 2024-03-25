erros = 0

while True:
    palavra = input("Digite a IFPB: ")
    if palavra == "IFPB":
        break
    erros += 1

print(f"Erros = {erros}")
