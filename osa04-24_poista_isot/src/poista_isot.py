# tee ratkaisu tänne
def poista_isot(lista):
    isot_poistettu = []
    for mjono in lista:
        if not mjono.isupper():
            isot_poistettu.append(mjono)

    return isot_poistettu


if __name__ == '__main__':
    lista = ["ABC", "def", "ISO", "TOINENISO",
             "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)
