# tee ratkaisu tänne
from datetime import datetime
from math import fabs, trunc


def oikea_pvm(aika: str, valimerkki: str):
    if valimerkki == '+':
        vuosisata = 1800
    elif valimerkki == '-':
        vuosisata = 1900
    elif valimerkki == 'A':
        vuosisata = 2000

    paiva = int(aika[:2])
    kuukausi = int(aika[2:4])
    vuosi = int(aika[4:]) + vuosisata

    try:
        oikea_aika = datetime(vuosi, kuukausi, paiva)
        return True
    except:
        return False


def onko_validi(hetu: str):
    if len(hetu) != 11:
        return False

    aika = hetu[:6]
    valimerkki = hetu[6]
    yksilonumero = hetu[7:10]
    tarkiste = hetu[-1]

    if valimerkki not in '+-A':
        return False

    if not oikea_pvm(aika, valimerkki):
        return False

    tarkistusjoukko = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    merkki = int(aika + yksilonumero) % 31
    return tarkiste == tarkistusjoukko[merkki]


if __name__ == '__main__':
    print(onko_validi('280479-099V'))
