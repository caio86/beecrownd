tipo1 = input()
tipo2 = input()
tipo3 = input()

if tipo1 == "vertebrado":
    # Vertebrados
    if tipo2 == "ave":
        # Aves
        if tipo3 == "carnivoro":
            # carnivoro
            print("aguia")
        else:
            # onivoro
            print("pomba")
    else:
        # mamiferos
        if tipo3 == "onivoro":
            # onivoro
            print("homem")
        else:
            # herbivoro
            print("vaca")
else:
    # Invertebrados
    if tipo2 == "inseto":
        # inseto
        if tipo3 == "hematofago":
            # hematofago
            print("pulga")
        else:
            # herbivoro
            print("lagarta")
    else:
        # anelideo
        if tipo3 == "hematofago":
            # hematofago
            print("sanguessuga")
        else:
            # onivoro
            print("minhoca")
