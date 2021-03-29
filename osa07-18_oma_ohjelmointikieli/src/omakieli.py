# tee ratkaisu tänne
from string import ascii_lowercase, ascii_uppercase as ascii, digits


def alusta_muuttujat():
    muuttujat = {}
    for c in ascii:
        muuttujat[c] = 0
    return muuttujat


def lue_kohdat(ohjelma: list):
    kohdat = {}
    for rivi in range(len(ohjelma)):
        osat = ohjelma[rivi].split(' ')
        komento = osat[0]
        if komento.endswith(':'):
            komento = komento.replace(':', '')
            kohdat[komento] = rivi

    return kohdat


def PRINT(muuttuja: str, muuttujat: dict, tulos: list):
    if muuttuja in muuttujat:
        tulos.append(muuttujat[muuttuja])
    elif muuttuja in digits:
        tulos.append(int(muuttuja))


def MOV(muuttuja: str, arvo: str, muuttujat: dict):
    if muuttuja in muuttujat:
        if arvo in ascii:
            muuttujat[muuttuja] = muuttujat[arvo]
        else:
            muuttujat[muuttuja] = int(arvo)


def ADD(muuttuja: str, arvo, muuttujat: dict):
    if muuttuja in muuttujat:
        if(arvo in ascii):
            muuttujat[muuttuja] += muuttujat[arvo]
        elif arvo in digits:
            muuttujat[muuttuja] += int(arvo)


def SUB(muuttuja: str, arvo, muuttujat: dict):
    if muuttuja in muuttujat:
        if(arvo in ascii):
            muuttujat[muuttuja] -= muuttujat[arvo]
        elif arvo in digits:
            muuttujat[muuttuja] -= int(arvo)


def MUL(muuttuja: str, arvo, muuttujat: dict):
    if muuttuja in muuttujat:
        if(arvo in ascii):
            muuttujat[muuttuja] *= muuttujat[arvo]
        elif arvo in digits:
            muuttujat[muuttuja] *= int(arvo)


def JUMP(kohta: str, kohdat: dict):
    global rivi
    if kohta in kohdat:
        rivi = kohdat[kohta]
    else:
        rivi += 1


def IF(arvo1: str, arvo2: str, vertailu: str, kohta: str, muuttujat: dict, kohdat: dict):
    a1 = int(arvo1) if arvo1.isnumeric() else muuttujat[arvo1]
    a2 = int(arvo2) if arvo2.isnumeric() else muuttujat[arvo2]

    osuma = False
    if vertailu == '==':
        if a1 == a2:
            osuma = True
    elif vertailu == '!=':
        if a1 != a2:
            osuma = True
    elif vertailu == '<':
        if a1 < a2:
            osuma = True
    elif vertailu == '<=':
        if a1 <= a2:
            osuma = True
    elif vertailu == '>':
        if a1 > a2:
            osuma = True
    elif vertailu == '>=':
        if a1 >= a2:
            osuma = True

    if osuma:
        JUMP(kohta, kohdat)


def suorita(ohjelma: list):
    global rivi
    muuttujat = alusta_muuttujat()
    kohdat = lue_kohdat(ohjelma)
    tulos = []
    rivi = 0
    while rivi < len(ohjelma):
        osat = ohjelma[rivi].split(' ')
        komento: str = osat[0]
        if komento == 'END':
            break
        elif komento == 'PRINT':
            PRINT(osat[1], muuttujat, tulos)
        elif komento == 'MOV':
            MOV(osat[1], osat[2], muuttujat)
        elif komento == 'ADD':
            ADD(osat[1], osat[2], muuttujat)
        elif komento == 'SUB':
            SUB(osat[1], osat[2], muuttujat)
        elif komento == 'MUL':
            MUL(osat[1], osat[2], muuttujat)
        elif komento == 'JUMP':
            JUMP(osat[1], kohdat)
        elif komento == 'IF':
            IF(osat[1], osat[3], osat[2], osat[5], muuttujat, kohdat)
        rivi += 1

    return tulos


if __name__ == '__main__':
    # testi koodia
    ohjelma3 = []
    ohjelma3.append("MOV A 1")
    ohjelma3.append("MOV B 1")
    ohjelma3.append("alku:")
    ohjelma3.append("PRINT A")
    ohjelma3.append("ADD B 1")
    ohjelma3.append("MUL A B")
    ohjelma3.append("IF B <= 10 JUMP alku")
    ohjelma3.append("END")
    tulos = suorita(ohjelma3)
    print(tulos)
