# tee ratkaisu tänne
from os import WIFSTOPPED


def lue_hedelmat():
    hedelmat = {}
    with open('hedelmat.csv') as tiedosto:
        for rivi in tiedosto:
            nimi, hinta = rivi.split(';')
            hedelmat[nimi] = float(hinta)

    return hedelmat


if __name__ == '__main__':
    print(lue_hedelmat())
