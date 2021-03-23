# tee ratkaisu tänne
from os import truncate


def suodata_virheelliset():
    with open('lottonumerot.csv') as tiedosto:
        korjatut = []
        for rivi in tiedosto:
            rivi = rivi.strip()
            osat = rivi.split(';')
            viikkonro = osat[0].split(' ')[1]
            numerot = osat[1].split(',')

            # viikkonumero pielessä
            if not viikkonro.isnumeric():
                continue

            # liian vähän numeroita
            if len(numerot) != 7:
                continue

            # numero(t) pielessä
            virheellinen = False
            for numero in numerot:
                if not numero.isnumeric():
                    virheellinen = True
                    continue
            # liian pieniä tai suuria numeroita
                if int(numero) < 1 or int(numero) > 39:
                    virheellinen = True
                    continue
            # sama numero kahdesti
                if numerot.count(numero) > 1:
                    virheellinen = True
                    continue

            if not virheellinen:
                korjatut.append(rivi)

    with open('korjatut_numerot.csv', 'w') as tiedosto:
        for rivi in korjatut:
            tiedosto.write(rivi + '\n')


if __name__ == '__main__':
    suodata_virheelliset()
