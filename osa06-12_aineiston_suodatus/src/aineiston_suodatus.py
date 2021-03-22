# tee ratkaisu tänne
def suodata_laskut():
    with open('laskut.csv') as tiedosto:
        oikeat = []
        vaarat = []
        for rivi in tiedosto:
            nimi, lasku, vastaus = rivi.split(';')
            if eval(lasku) == int(vastaus):
                oikeat.append(rivi)
            else:
                vaarat.append(rivi)

        with open('oikeat.cvs', 'w') as tiedosto:
            for rivi in oikeat:
                tiedosto.write(rivi)

        with open('vaarat.csv', 'w') as tiedosto:
            for rivi in vaarat:
                tiedosto.write(rivi)


if __name__ == '__main__':
    suodata_laskut()
