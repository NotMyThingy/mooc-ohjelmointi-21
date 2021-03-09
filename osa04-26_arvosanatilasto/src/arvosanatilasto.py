# Kirjoita ratkaisu tähän
def lue_syotteet():
    syotteet = []
    while True:
        luvut = input('Koepisteet ja harjoitusten määrä: ')
        if luvut == '':
            break

        syotteet.append(luvut)
    return syotteet


def laske_kokonaispisteet(syotteet: list):
    kokonaispisteet = []
    for rivi in syotteet:
        arvot = rivi.split(' ')
        koepisteet = int(arvot[0])
        harjoitusten_lkm = int(arvot[1])
        if koepisteet < 10:
            kokonaispisteet.append(0)
        else:
            harjoituspisteet = harjoitus_pisteet(harjoitusten_lkm)
            kokonaispisteet.append(koepisteet + harjoituspisteet)

    return kokonaispisteet


def harjoitus_pisteet(harjoitusten_lkm: int):
    pisteet: int
    if harjoitusten_lkm < 10:
        pisteet = 0
    elif harjoitusten_lkm < 20:
        pisteet = 1
    elif harjoitusten_lkm < 30:
        pisteet = 2
    elif harjoitusten_lkm < 40:
        pisteet = 3
    elif harjoitusten_lkm < 50:
        pisteet = 4
    elif harjoitusten_lkm < 60:
        pisteet = 5
    elif harjoitusten_lkm < 70:
        pisteet = 6
    elif harjoitusten_lkm < 80:
        pisteet = 7
    elif harjoitusten_lkm < 90:
        pisteet = 8
    elif harjoitusten_lkm < 100:
        pisteet = 9
    else:
        pisteet = 10

    return pisteet


def main():
    syotteet = lue_syotteet()
    print(syotteet)
    kokonaispisteet = laske_kokonaispisteet(syotteet)
    print(kokonaispisteet)


main()
