# tee ratkaisu tänne
from string import ascii_uppercase as ascii, punctuation


def alusta_muuttujat():
    muuttujat = {}
    for c in ascii:
        muuttujat[c] = 0
    return muuttujat


def suorita(ohjelma: list):
    muuttujat = alusta_muuttujat()
    tulostettavat = []
    kohta = {}
    i = 0
    while i < len(ohjelma):
        print(i)
        osat = ohjelma[i].split(' ')
        komento: str = osat[0]
        if komento == 'END':
            break
        elif komento == 'PRINT':
            tulostettavat.append(muuttujat[osat[1]])
            i += 1
        elif komento == 'MOV':
            muuttuja = osat[1]
            arvo = int(osat[2])
            muuttujat[muuttuja] = arvo
            i += 1
        elif komento == 'ADD':
            muuttuja = osat[1]
            arvo = osat[2]
            if arvo.isdigit():
                muuttujat[muuttuja] += int(arvo)
            else:
                muuttujat[muuttuja] += muuttujat[arvo]
            i += 1
        elif komento == 'SUB':
            muuttuja = osat[1]
            arvo = osat[2]
            if arvo.isdigit():
                muuttujat[muuttuja] -= int(arvo)
            else:
                muuttujat[muuttuja] -= muuttujat[arvo]
            i += 1
        elif komento == 'MUL':
            muuttuja = osat[1]
            arvo = osat[2]
            if arvo.isdigit():
                muuttujat[muuttuja] *= int(arvo)
            else:
                muuttujat[muuttuja] *= muuttujat[arvo]
            i += 1
        elif komento.islower():
            i += 1
            kohta[komento] = i
            print(i)
            print(kohta)
        elif komento == 'JUMP':
            indeksi = osat[1]
            if indeksi in kohta:
                i = kohta[indeksi]
        elif komento == 'IF':
            arvo1 = osat[1]
            arvo2 = osat[3]
            if arvo1 osat[2] arvo2

    return tulostettavat


if __name__ == '__main__':
    alusta_muuttujat()
    ohjelma1 = []
    ohjelma1.append("MOV A 1")
    ohjelma1.append("MOV B 2")
    ohjelma1.append("alku:")
    ohjelma1.append("PRINT A")
    ohjelma1.append("PRINT B")
    ohjelma1.append("ADD A B")
    ohjelma1.append("MUL A B")
    ohjelma1.append("PRINT A")
    ohjelma1.append("END")
    tulos = suorita(ohjelma1)
    print(tulos)
