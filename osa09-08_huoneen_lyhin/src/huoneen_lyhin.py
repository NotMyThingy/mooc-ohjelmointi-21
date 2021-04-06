# TEE RATKAISUSI TÄHÄN:
class Henkilo:
    def __init__(self, nimi: str, pituus: int):
        self.nimi = nimi
        self.pituus = pituus

    def __str__(self):
        return f'{self.nimi} ({self.pituus} cm)'


class Huone:

    def __init__(self) -> None:
        self.henkilot = []

    def lisaa(self, henkilo: Henkilo):
        self.henkilot.append(henkilo)

    def on_tyhja(self):
        return len(self.henkilot) == 0

    def tulosta_tiedot(self):
        print(f'Huoneessa {len(self.henkilot)} henkilöä, yhteispituus {sum(henkilo.pituus for henkilo in self.henkilot)} cm')
        for henkilo in self.henkilot:
            print(henkilo)

    def lyhin(self):
        if len(self.henkilot) == 0:
            return None

        lyhin = self.henkilot[0]
        for henkilo in self.henkilot:
            if henkilo.pituus < lyhin.pituus:
                lyhin = henkilo

        return lyhin

    def poista_lyhin(self):
        lyhin_henkilo = self.lyhin()
        try:
            self.henkilot.remove(lyhin_henkilo)
            return lyhin_henkilo
        except:
            return None


if __name__ == "__main__":
    huone = Huone()

    huone.lisaa(Henkilo("Lea", 183))
    huone.lisaa(Henkilo("Kenya", 182))
    huone.lisaa(Henkilo("Nina", 172))
    huone.lisaa(Henkilo("Auli", 186))
    huone.tulosta_tiedot()

    print()

    poistettu = huone.poista_lyhin()
    print(f"Otettiin huoneesta {poistettu.nimi}")

    print()

    huone.tulosta_tiedot()
