# tee ratkaisu tänne
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koetiedot = input("Koepisteet: ")

opiskelijat = {}
with open(opiskelijatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        opiskelijat[osat[0]] = f'{osat[1]} {osat[2].strip()}'

tehtavapisteet = {}
with open(tehtavatiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        summa = 0
        for luku in osat[1:]:
            summa += int(luku)
        tehtavapisteet[osat[0]] = summa

koepisteet = {}
with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = rivi.split(';')
        if osat[0] == 'opnro':
            continue
        pisteet = 0
        for luku in osat[1:]:
            pisteet += int(luku)
        koepisteet[osat[0]] = pisteet

arvosanat = {}
for opnro in opiskelijat:
    pisteet = koepisteet[opnro] + tehtavapisteet[opnro] // 4
    arvosana = 0
    rajat = [15, 18, 21, 24, 28]
    while arvosana < 5 and pisteet >= rajat[arvosana]:
        arvosana += 1

    arvosanat[opnro] = arvosana

for opnro, nimi in opiskelijat.items():
    print(f'{nimi} {arvosanat[opnro]}')
