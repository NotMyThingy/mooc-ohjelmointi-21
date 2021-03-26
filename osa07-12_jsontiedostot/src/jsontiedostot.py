# tee ratkaisu tänne
import json


def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as f:
        sisalto = f.read()
    henkilot = json.loads(sisalto)
    for rivi in henkilot:
        nimi = rivi['nimi']
        ika = rivi['ika']
        harrastukset = ', '.join(rivi['harrastukset'])
        print(f'{nimi} {ika} vuotta ({harrastukset})')


if __name__ == '__main__':
    tulosta_henkilot('tiedosto1.json')
