# Kirjoita ratkaisu tähän
def tulosta(alku, loppu):
    for i in range(alku, loppu):
        if i != 0:
            print(i)


luku = int(input("Anna luku: "))
tulosta(-luku, luku + 1)
