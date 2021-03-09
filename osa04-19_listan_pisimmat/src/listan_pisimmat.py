# tee ratkaisu tänne

def pisimmat(nimet: list):
    pisimmat = []

    for nimi in nimet:
        if pisimmat == [] or len(nimi) > len(pisimmat[0]):
            pisimmat = [nimi]
        elif len(nimi) == len(pisimmat[0]):
            pisimmat.append(nimi)

    return pisimmat


if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos)  # ['emilia', 'juhani']
