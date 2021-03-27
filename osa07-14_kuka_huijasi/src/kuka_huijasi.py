# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta


def huijarit():
    aloitukset = []
    palautukset = []
    with open('tentin_aloitus.csv') as aloitus_tiedosto, open('palautus.csv') as palautus_tiedosto:
        for aloitus in aloitus_tiedosto:
            aloitukset.append(aloitus.strip().split(';'))
        for palautus in palautus_tiedosto:
            palautukset.append(palautus.strip().split(';'))

    huijarit = []
    for aloitus in aloitukset:
        nimi = aloitus[0]
        aloitus_aika = datetime.strptime(aloitus[1], '%H:%M')

        for palautus in palautukset:
            verrattava = palautus[0]
            palautus_aika = datetime.strptime(palautus[-1], '%H:%M')

            if nimi == verrattava:
                ero = palautus_aika - aloitus_aika

                if (ero.seconds / 3600) > 3 and verrattava not in huijarit:
                    huijarit.append(verrattava)

    return huijarit


if __name__ == '__main__':
    print(huijarit())
