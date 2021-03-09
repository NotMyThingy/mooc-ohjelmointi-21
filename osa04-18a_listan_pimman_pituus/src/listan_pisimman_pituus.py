# tee ratkaisu tänne
def pisimman_pituus(lista):
    pisin = 0
    for sana in lista:
        if len(sana) > pisin:
            pisin = len(sana)

    return pisin


if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimman_pituus(lista)
    print(tulos)
