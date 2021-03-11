from typing import List


def lue_arvot():
    arvot = []
    while True:
        luettu = input('Koepisteet ja harjoitusten määrä: ')
        if luettu == '':
            break
        arvot.append(luettu)
    return arvot


def muunna_pisteiksi(lista: list, indeksi: int, jaetaan: bool):
    pisteet = []
    for rivi in lista:
        if jaetaan:
            pisteet.append(int(rivi.split(' ')[indeksi]) // 10)
        else:
            pisteet.append(int(rivi.split(' ')[indeksi]))
    return pisteet


def laske_arvosanajakauma(koepisteet: list, harjoituspisteet: list):
    arvosanat = [0] * 6
    for i in range(len(koepisteet)):
        pisteet = koepisteet[i] + harjoituspisteet[i]
        if koepisteet[i] < 10 or pisteet < 15:
            arvosanat[0] += 1
        elif pisteet < 18:
            arvosanat[1] += 1
        elif pisteet < 21:
            arvosanat[2] += 1
        elif pisteet < 24:
            arvosanat[3] += 1
        elif pisteet < 28:
            arvosanat[4] += 1
        elif pisteet < 31:
            arvosanat[5] += 1
        else:
            print('Something extremely weird just happened...')
    return arvosanat


def laske_pisteiden_ka(koepisteet: list, harjotuspisteet: list):
    summa = sum(koepisteet) + sum(harjotuspisteet)
    return summa / len(koepisteet)


def laske_hyvaksymisprosentti(arvosanat: list):
    return sum(arvosanat[1:]) / sum(arvosanat) * 100


############################################################
#                                                          #
#                       THE TILASTO                        #
#                                                          #
############################################################

def tulosta_tilasto(koepisteet: list, harjoituspisteet: list, arvosanat: list):
    ka = laske_pisteiden_ka(koepisteet, harjoituspisteet)
    hy_prosentti = laske_hyvaksymisprosentti(arvosanat)
    print('Tilasto:')
    print(f'Pisteiden keskiarvo: {ka:.1f}')
    print(f'Hyväksymisprosentti: {hy_prosentti:.1f}')
    print('Arvosanajakauma:')
    arvosana = 5
    while arvosana >= 0:
        print(f'{arvosana}: {arvosanat[arvosana] * "*"}')
        arvosana -= 1


def main():
    arvot = lue_arvot()
    koepisteet = muunna_pisteiksi(arvot, 0, False)
    harjoituspisteet = muunna_pisteiksi(arvot, 1, True)
    arvosanat = laske_arvosanajakauma(koepisteet, harjoituspisteet)
    tulosta_tilasto(koepisteet, harjoituspisteet, arvosanat)


main()
