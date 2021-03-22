# tee ratkaisu tänne
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")
kurssitiedot = input("Kurssin tiedot: ")


def arvosana(pisteet):
    a = 0
    pisterajat = [15, 18, 21, 24, 28]
    while a < 5 and pisteet >= pisterajat[a]:
        a += 1

    return a


def pisteiksi(lkm):
    return lkm // 4


opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        opiskelijat[osat[0]] = f'{osat[1]} {osat[2].strip()}'

tehtavat = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        summa = 0
        for luku in osat[1:]:
            summa += int(luku)
        tehtavat[osat[0]] = summa

kokeet = {}
with open(koepisteet) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        pisteet = 0
        for luku in osat[1:]:
            pisteet += int(luku)
        kokeet[osat[0]] = pisteet

kurssi = []
with open(kurssitiedot) as tiedosto:
    for rivi in tiedosto:
        i = rivi.index(':') + 1
        kurssi.append(rivi[i:].strip())

with open('tulos.txt', 'w') as tulokset, open('tulos.csv', 'w') as tiedosto:
    otsikko = f"{kurssi[0]}, {kurssi[1]} opintopistettä"
    tulokset.write(otsikko + '\n')
    tulokset.write(f'{"=" * len(otsikko)}\n')
    tulokset.write(
        f"{'nimi':30}{'teht_lkm':10}{'teht_pist':10}{'koe_pist':10}{'yht_pist':10}{'arvosana'}\n")
    for opnro, nimi in opiskelijat.items():
        tehtavia = tehtavat[opnro]
        teht_pist = pisteiksi(tehtavat[opnro])
        koe_pist = kokeet[opnro]
        yht_pist = koe_pist + teht_pist
        tulokset.write(
            f'{nimi:30}{tehtavia:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana(yht_pist):<10}\n')
        tiedosto.write(f'{opnro};{nimi};{arvosana(yht_pist)}\n')
