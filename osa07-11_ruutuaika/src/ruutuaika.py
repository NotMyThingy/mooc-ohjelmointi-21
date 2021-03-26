# tee ratkaisu tänne,
from datetime import datetime, timedelta


def lue_ruutuaika(paivia: int, aloitus_pvm: datetime):
    ruutuajat = {}
    for i in range(paivia):
        aika = aloitus_pvm.strftime("%d.%m.%Y")
        ajat = input(f'Ruutuaika {aika}: ')
        ruutuajat[aika] = ajat.replace(' ', '/')
        aloitus_pvm += timedelta(1)

    return ruutuajat


def laske_minuutit(ruutuaika: dict):
    minuutit = []
    for pv in ruutuaika:
        summa = 0
        ajat = ruutuaika[pv].split('/')
        for aika in ajat:
            summa += int(aika)
        minuutit.append(summa)

    return minuutit


def main():
    tiedosto = input('Tiedosto: ')
    pvm = input('Aloituspäivä: ')
    aloitus = datetime.strptime(pvm, '%d.%m.%Y')
    paivia = int(input('Montako päivää: '))

    print('Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):')
    ruutuaika = lue_ruutuaika(paivia, aloitus)
    minuutit = laske_minuutit(ruutuaika)

    with open(tiedosto, 'w') as tiedosto:
        tiedosto.write(f'Ajanjakso: {aloitus.strftime("%d.%m.%Y")} - {(aloitus + timedelta(paivia -1)).strftime("%d.%m.%Y")}\n')
        tiedosto.write(f'Yht. minuutteja: {sum(minuutit)}\n')
        tiedosto.write(f'Keskim. minuutteja: {sum(minuutit) / len(minuutit):.1f}\n')
        for paiva in ruutuaika:
            tiedosto.write(f'{paiva}: {ruutuaika[paiva]}\n')


if __name__ == '__main__':
    main()
