# tee ratkaisu tänne
if False:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
    koetiedot = "koepisteet1.csv"


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

koepisteet = {}
with open(koetiedot) as tiedosto:
    for rivi in tiedosto:
        osat = split(';')
        if osat[0] == 'opnro':
            continue
        pisteet = 0
        for luku in osat[1:]:
            pisteet += int(luku)
        koepisteet[osat[0]] = pisteet

for opnro, nimi in opiskelijat.items():
    print(f'{nimi} {tehtavat[opnro]} {koepisteet[opnro]}')
