# tee ratkaisu tänne
def lue_luvut():
    with open('matriisi.txt') as tiedosto:
        luvut = []
        for rivi in tiedosto:
            lukurivi = []
            rivi = rivi.split(',')
            for luku in rivi:
                lukurivi.append(int(luku))
            luvut.append(lukurivi)

    return luvut


def yhdista(luvut: list):
    lista = []
    for rivi in luvut:
        lista += rivi

    return lista


def rivisummat():
    luvut = lue_luvut()
    rivisummat = []
    for rivi in luvut:
        rivisummat.append(sum(rivi))

    return rivisummat


def summa():
    lista = yhdista(lue_luvut())
    return sum(lista)


def maksimi():
    lista = yhdista(lue_luvut())
    return max(lista)


if __name__ == '__main__':
    print(summa())
    print('#################################')
    print(rivisummat())
    print('#################################')
    print(maksimi())
