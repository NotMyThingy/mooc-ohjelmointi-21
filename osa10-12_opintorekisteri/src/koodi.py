# tee ratkaisusi tänne
class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int) -> None:
        self.__kurssi = kurssi
        self.__arvosana = arvosana
        self.__opintopisteet = opintopisteet

    def kurssi(self):
        return self.__kurssi

    def arvosana(self):
        return self.__arvosana

    def opintopisteet(self):
        return self.__opintopisteet

    def __str__(self) -> str:
        return f'{self.__kurssi} ({self.__opintopisteet} op) arvosana {self.__arvosana}'


class Opintorekisteri:
    def __init__(self) -> None:
        self.__kurssit = {}

    def lisaa_suoritus(self, kurssi: str, arvosana: int, opintopisteet: int):
        if kurssi in self.__kurssit and self.__kurssit[kurssi].arvosana() > arvosana:
            return

        self.__kurssit[kurssi] = Suoritus(kurssi, arvosana, opintopisteet)

    def hae_suoritus(self, kurssi: str):
        if kurssi not in self.__kurssit:
            return None

        return self.__kurssit[kurssi]

    def hae_tilastot(self):
        kursseja = len(self.__kurssit)
        opintopisteet = 0
        arvosanojen_summa = 0
        arvosanat = [0, 0, 0, 0, 0, 0]

        for kurssi in self.__kurssit.values():
            opintopisteet += kurssi.opintopisteet()
            arvosanojen_summa += kurssi.arvosana()
            arvosanat[kurssi.arvosana()] += 1

        return {
            'kursseja': kursseja,
            'opintopisteet': opintopisteet,
            'keskiarvo': arvosanojen_summa / kursseja,
            'arvosanat': arvosanat
        }


class Sovellus:
    def __init__(self) -> None:
        self.__rekisteri = Opintorekisteri()

    def ohje(self):
        print('1 lisää suoritus')
        print('2 hae suoritus')
        print('3 tilastot')
        print('0 lopetus')

    def uusi_suoritus(self):
        kurssi = input('kurssi: ')
        arvosana = int(input('arvosana: '))
        opintopisteet = int(input('opintopisteet: '))
        self.__rekisteri.lisaa_suoritus(kurssi, arvosana, opintopisteet)

    def hae_suoritus(self):
        kurssi = input('kurssi: ')
        suoritus = self.__rekisteri.hae_suoritus(kurssi)
        if suoritus == None:
            print('ei suoritusta')
        else:
            print(suoritus)

    def tilasto(self):
        t = self.__rekisteri.hae_tilastot()

        print(f'suorituksia {t["kursseja"]} kurssilta, yhteensä {t["opintopisteet"]} opintopistettä')
        print(f'keskiarvo {t["keskiarvo"]:.1f}')
        print('arvosanajakauma')
        for i in range(5, 0, -1):
            arvosanan_esiintyminen = t['arvosanat'][i]
            rivi = 'x' * arvosanan_esiintyminen
            print(f'{i}: {rivi}')

    def suorita(self):
        self.ohje()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                break

            if komento == '1':
                self.uusi_suoritus()
            elif komento == '2':
                self.hae_suoritus()
            elif komento == '3':
                self.tilasto()
            else:
                self.ohje()


o = Sovellus()
o.suorita()
