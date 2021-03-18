# tee ratkaisu tänne
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koetiedot = input("Koepisteet: ")


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
with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        pisteet = 0
        for luku in osat[1:]:
            pisteet += int(luku)
        kokeet[osat[0]] = pisteet


print(f"{'nimi':30}{'teht_lkm':10}{'teht_pist':10}{'koe_pist':10}{'yht_pist':10}{'arvosana'}")
for opnro, nimi in opiskelijat.items():
    tehtavia = tehtavat[opnro]
    teht_pist = pisteiksi(tehtavat[opnro])
    koe_pist = kokeet[opnro]
    yht_pist = koe_pist + teht_pist
    print(f'{nimi:30}{tehtavia:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana(yht_pist):<10}')
