class Tehtava:
    id = 0

    @classmethod
    def luo_id(cls):
        Tehtava.id += 1
        return Tehtava.id

    def __init__(self, kuvaus: str, koodari: str, tyomaara: int) -> None:
        self.id = Tehtava.luo_id()
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.valmis = False

    def on_valmis(self):
        return self.valmis

    def merkkaa_valmiiksi(self):
        self.valmis = True

    def __str__(self) -> str:
        status = 'VALMIS' if self.on_valmis() else 'EI VALMIS'
        return f'{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {status}'


class Tilauskirja:
    def __init__(self) -> None:
        self.tehtavat = []

    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        self.tehtavat.append(Tehtava(kuvaus, koodari, tyomaara))

    def kaikki_tilaukset(self):
        return self.tehtavat

    def valmiit_tilaukset(self):
        return [t for t in self.tehtavat if t.on_valmis()]

    def ei_valmiit_tilaukset(self):
        return [t for t in self.tehtavat if not t.on_valmis()]

        # palauttaa listan koodareista. Sama koodari saa olla listalla vain kerran -> set
    def koodarit(self):
        return list(set([t.koodari for t in self.tehtavat]))

    def merkkaa_valmiiksi(self, id: int):
        try:
            [t for t in self.tehtavat if t.id == id][0].merkkaa_valmiiksi()
        except:
            raise ValueError('id ei kelpaa')

    def koodarin_status(self, koodari: str):
        if koodari not in self.koodarit():
            raise ValueError('koodari ei kelpaa')

        valmiit = [t for t in self.tehtavat if t.koodari ==
                   koodari and t.on_valmis()]
        kesken = [t for t in self.tehtavat if t.koodari ==
                  koodari and not t.on_valmis()]

        valmiit_tunnit = sum(t.tyomaara for t in valmiit)
        kesken_tunnit = sum(t.tyomaara for t in kesken)

        return len(valmiit), len(kesken), valmiit_tunnit, kesken_tunnit


class Sovellus:
    def __init__(self) -> None:
        self.tilauskirja = Tilauskirja()

    def menu(self):
        print('komennot:')
        print('0 lopetus')
        print('1 lisää tilaus')
        print('2 listaa valmiit')
        print('3 listaa ei valmiit')
        print('4 merkitse tehtävä valmiiksi')
        print('5 koodarit')
        print('6 koodarin status')

    def lisaa_uusi_tehtava(self):
        try:
            kuvaus = input('kuvaus: ')
            koodari, tyomaara = input('koodari ja työmääräarvio: ').split(' ')
            self.tilauskirja.lisaa_tilaus(kuvaus, koodari, int(tyomaara))
        except:
            print('virheellinen syöte\n')
            print('komento: 1')
            self.lisaa_uusi_tehtava()

    def listaa_valmiit(self):
        valmiit = self.tilauskirja.valmiit_tilaukset()
        if not valmiit:
            print('ei valmiita')
        else:
            for tehtava in valmiit:
                print(tehtava)

    def listaa_ei_valmiit(self):
        kesken = self.tilauskirja.ei_valmiit_tilaukset()
        if not kesken:
            print('ei kesken')
        else:
            for tehtava in kesken:
                print(tehtava)

    def merkitse_valmiiksi(self):
        tunniste = int(input('tunniste: '))
        self.tilauskirja.merkkaa_valmiiksi(tunniste)
        print('merkitty valmiiksi')

    def tulosta_koodarit(self):
        for koodari in self.tilauskirja.koodarit():
            print(koodari)

    def tulosta_koodarin_status(self):
        koodari = input('koodari: ')
        s = self.tilauskirja.koodarin_status(koodari)
        print(
            f'työt: valmiina {s[0]} ei valmiina {s[1]}, tunteja: tehty {s[2]} tekemättä {s[3]}')

    def suorita(self):
        self.menu()
        while True:
            print()
            komento = input('komento: ')
            if komento == '0':
                break

            if komento == '1':
                self.lisaa_uusi_tehtava()
            elif komento == '2':
                self.listaa_valmiit()
            elif komento == '3':
                self.listaa_ei_valmiit()
            elif komento == '4':
                self.merkitse_valmiiksi()
            elif komento == '5':
                self.tulosta_koodarit()
            elif komento == '6':
                self.tulosta_koodarin_status()


if __name__ == "__main__":
    s = Sovellus()
    s.suorita()
