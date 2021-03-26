# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta


def viralliset_pisteet():
    with open('tentin_aloitus.csv') as aloitus, open('palautus.csv') as palautus:
        aloitusajat = {}
        for rivi in csv.reader(aloitus, delimiter=';'):
            nimi = rivi[0]
            aika = datetime.strptime(rivi[1], '%H:%M')
            aloitusajat[nimi] = aika

        tehtavapisteet = {}
        for rivi in csv.reader(palautus, delimiter=';'):
            nimi = rivi[0]
            tehtava_nro = rivi[1]
            pisteet = int(rivi[2])
            aika = datetime.strptime(rivi[3], '%H:%M')

            if aika - aloitusajat[nimi] > timedelta(hours=3):
                continue

            if nimi not in tehtavapisteet:
                tehtavapisteet[nimi] = {tehtava_nro: pisteet}
            elif tehtava_nro not in tehtavapisteet[nimi]:
                tehtavapisteet[nimi][tehtava_nro] = pisteet
            elif pisteet > tehtavapisteet[nimi][tehtava_nro]:
                tehtavapisteet[nimi][tehtava_nro] = pisteet

    kokonaispisteet = {}
    for nimi in tehtavapisteet:
        summa = 0
        for pisteet in tehtavapisteet[nimi]:
            summa += tehtavapisteet[nimi][pisteet]
        kokonaispisteet[nimi] = summa

    return kokonaispisteet


if __name__ == '__main__':
    print(viralliset_pisteet())
