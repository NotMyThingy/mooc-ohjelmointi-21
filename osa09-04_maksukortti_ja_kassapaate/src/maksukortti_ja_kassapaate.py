# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        if self.saldo >= maara:
            self.saldo -= maara
            return True

        return False


class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        # Edullinen lounas maksaa 2.50 euroa
        # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        edulllinen = 2.50
        if maksu < edulllinen:
            return maksu

        self.rahaa += edulllinen
        self.edulliset += 1

        return maksu - edulllinen

    def syo_maukkaasti(self, maksu: float):
        # Maukas lounas maksaa 4.30 euroa
        # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        maukas = 4.30
        if maksu < maukas:
            return maksu

        self.rahaa += maukas
        self.maukkaat += 1

        return maksu - maukas

    def syo_edullisesti_kortilla(self, kortti: Maksukortti):
        # Edullinen lounas maksaa 2.50 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        edullinen = 2.50
        if kortti.ota_rahaa(edullinen):
            self.edulliset += 1
            return True

        return False

    def syo_maukkaasti_kortilla(self, kortti: Maksukortti):
        # Maukas lounas maksaa 4.30 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        maukas = 4.30
        if kortti.ota_rahaa(maukas):
            self.maukkaat += 1
            return True

        return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        kortti.lataa_rahaa(summa)
        self.rahaa += summa


if __name__ == "__main__":
    exactum = Kassapaate()

    vaihtorahaa = exactum.syo_edullisesti(10)
    print("Vaihtorahaa jäi", vaihtorahaa)

    kortti = Maksukortti(7)

    tulos = exactum.syo_maukkaasti_kortilla(kortti)
    print("Riittikö raha:", tulos)
    tulos = exactum.syo_maukkaasti_kortilla(kortti)
    print("Riittikö raha:", tulos)
    tulos = exactum.syo_edullisesti_kortilla(kortti)
    print("Riittikö raha:", tulos)

    print("Kassassa rahaa", exactum.rahaa)
    print("Edullisia lounaita myyty", exactum.edulliset)
    print("Maukkaita lounaita myyty", exactum.maukkaat)
