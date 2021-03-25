# tee ratkaisu tänne,
from datetime import datetime, timedelta

try:
    tiedosto = input('Tiedosto: ')
except:
    raise FileNotFoundError('Epäkelpo tiedoston nimi')

try:
    pvm = input('Aloituspäivä: ')
    aloitus = datetime.strptime(pvm, '%d.%m.%Y')
except:
    raise ValueError('päivämäärä ei kelpaa')

paivia = int(input('Montako päivää: '))
lopetus = aloitus + timedelta(paivia)

with open('kesakuun_loppu.txt', 'w') as tiedosto:
    tiedosto.write(
        f'Ajanjakso: {aloitus.strftime("%d.%m.%Y")} - {lopetus.strftime("%d.%m.%Y")}')

    print('Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):')
    for i in range(paivia):
        aika = aloitus.strftime("%d.%m.%Y")
        ajat = input(f'Ruutuaika {aika}: ')
        ruutuajat[aika] = ajat.replace(' ', '/')
        aloitus += timedelta(1)
