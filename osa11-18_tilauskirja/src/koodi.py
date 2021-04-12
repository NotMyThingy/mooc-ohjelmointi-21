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
        for tehtava in self.tehtavat:
            if tehtava.id == id:
                tehtava.merkkaa_valmiiksi()
                return
        
        raise ValueError('id ei kelpaa')

    def koodarin_status(self, koodari: str):
        if koodari not in self.koodarit():
            raise ValueError('koodari ei kelpaa')
        
        valmiit = [t for t in self.tehtavat if t.koodari == koodari and t.on_valmis()]
        kesken = [t for t in self.tehtavat if t.koodari == koodari and not t.on_valmis()]

        valmiit_tunnit = sum(t.tyomaara for t in valmiit)
        kesken_tunnit = sum(t.tyomaara for t in kesken)
        
        return len(valmiit), len(kesken), valmiit_tunnit, kesken_tunnit


if __name__ == "__main__":
    tilaukset = Tilauskirja()
    tilaukset.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
    tilaukset.lisaa_tilaus("tee mobiilisovellus työaikakirjanpitoon", "Antti", 25)
    tilaukset.lisaa_tilaus("tee ohjelma matematiikan harjoitteluun", "Antti", 100)
    tilaukset.lisaa_tilaus("tee uusi facebook", "Erkki", 1000)

    tilaukset.merkkaa_valmiiksi(1)
    tilaukset.merkkaa_valmiiksi(2)

    status = tilaukset.koodarin_status("Antti")
    print(status)
