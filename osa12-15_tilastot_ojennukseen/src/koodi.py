import json


class Pelaaja:
    def __init__(self, nimi: str, nat: str, assists: int, goals: int, penalties: int, team: str, games: int) -> None:
        self.nimi = nimi
        self.kansalaisuus = nat
        self.syotot = assists
        self.maalit = goals
        self.jaahyt = penalties
        self.joukkue = team
        self.peleja = games

    def pisteet(self):
        return self.maalit + self.syotot

    def __str__(self) -> str:
        return f'{self.nimi:20} {self.joukkue}  {self.maalit:2} + {self.syotot:2} = {self.pisteet():3}'


class Liigatilasto:
    def __init__(self) -> None:
        self.pelaajat = []

    def lue_tiedosto(self, tiedosto: str) -> None:
        with open(tiedosto) as t:
            data = t.read()
        pelaaja_data = json.loads(data)
        for pelaaja in pelaaja_data:
            self.pelaajat.append(Pelaaja(pelaaja['name'],
                                         pelaaja['nationality'],
                                         pelaaja['assists'],
                                         pelaaja['goals'],
                                         pelaaja['penalties'],
                                         pelaaja['team'],
                                         pelaaja['games']))

    def koko(self) -> str:
        return len(self.pelaajat)

    def hae_pelaaja(self, nimi: str) -> str:
        return list(pelaaja for pelaaja in self.pelaajat if pelaaja.nimi == nimi)[0]

    def hae_joukkueet(self):
        return sorted(list(set([pelaaja.joukkue for pelaaja in self.pelaajat])))

    def hae_maat(self):
        return sorted(list(set([pelaaja.kansalaisuus for pelaaja in self.pelaajat])))

    def hae_pelaajat(self, joukkue: str):
        return sorted(list([pelaaja for pelaaja in self.pelaajat if pelaaja.joukkue == joukkue]),
                      key=lambda pelaaja: pelaaja.pisteet(), reverse=True)

    def hae_sama_kansalaisuus(self, maa):
        return sorted(list([pelaaja for pelaaja in self.pelaajat if pelaaja.kansalaisuus == maa]),
                      key=lambda pelaaja: pelaaja.pisteet(), reverse=True)

    def eniten_pisteita(self, maara: int):
        return sorted(list([pelaaja for pelaaja in self.pelaajat]), key=lambda pelaaja: (pelaaja.pisteet(), pelaaja.maalit), reverse=True)[0:maara]

    def eniten_maaleja(self, maara: int):
        return sorted(list([pelaaja for pelaaja in self.pelaajat]), key=lambda pelaaja: (pelaaja.maalit, -pelaaja.peleja), reverse=True)[0:maara]


class Sovellus:
    def __init__(self) -> None:
        self.tilasto = Liigatilasto()

    def menu(self):
        print('komennot:')
        print('0 lopeta')
        print('1 hae pelaaja')
        print('2 joukkueet')
        print('3 maat')
        print('4 joukkueen pelaajat')
        print('5 maan pelaajat')
        print('6 eniten pisteitä')
        print('7 eniten maaleja')

    def tulosta_pelaajan_tiedot(self):
        nimi = input('nimi: ')
        print()
        res = self.tilasto.hae_pelaaja(nimi)
        if res == None:
            res = 'nimellä ei löytynyt yhtään pelaajaa'
        print(res)

    def tulosta_joukkueet(self):
        print()
        for joukkue in self.tilasto.hae_joukkueet():
            print(joukkue)

    def tulosta_kansalaisuudet(self):
        print()
        for maa in self.tilasto.hae_maat():
            print(maa)

    def tulosta_joukkueen_pelaajat(self):
        joukkue = input('joukkue: ')
        print()
        for pelaaja in self.tilasto.hae_pelaajat(joukkue):
            print(pelaaja)

    def tulosta_sama_kansalaisuus(self):
        maa = input('maa: ')
        print()
        for maa in self.tilasto.hae_sama_kansalaisuus(maa):
            print(maa)

    def tulosta_eniten_pisteita(self):
        maara = int(input('kuinka monta: '))
        print()
        for pelaaja in self.tilasto.eniten_pisteita(maara):
            print(pelaaja)

    def tulosta_eniten_maaleja(self):
        maara = int(input('kuinka monta: '))
        print()
        for pelaaja in self.tilasto.eniten_maaleja(maara):
            print(pelaaja)

    def suorita(self):
        tiedosto = input('tiedosto: ')
        try:
            self.tilasto.lue_tiedosto(tiedosto)
            print(f'luettiin {self.tilasto.koko()} pelaajan tiedot\n')
        except:
            print('tiedostoa ei löydy!')
            self.suorita()

        self.menu()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                break
            if komento == '1':
                self.tulosta_pelaajan_tiedot()
            elif komento == '2':
                self.tulosta_joukkueet()
            elif komento == '3':
                self.tulosta_kansalaisuudet()
            elif komento == '4':
                self.tulosta_joukkueen_pelaajat()
            elif komento == '5':
                self.tulosta_sama_kansalaisuus()
            elif komento == '6':
                self.tulosta_eniten_pisteita()
            elif komento == '7':
                self.tulosta_eniten_maaleja()
            else:
                self.menu()


s = Sovellus()
s.suorita()
