# tee ratkaisu tänne
def parilliset(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)
