# TEE RATKAISUSI TÄHÄN:
import random


class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)

    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            else:
                pass  # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")


class PisinSana(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1

        if len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2


class EnitenVokaaleja(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        vokaalit = 'aeiouyåäö'
        vokaalit1 = 0
        vokaalit2 = 0

        for vokaali in vokaalit:
            vokaalit1 += pelaaja1_sana.count(vokaali)
            vokaalit2 += pelaaja2_sana.count(vokaali)

        if vokaalit1 > vokaalit2:
            return 1

        if vokaalit1 < vokaalit2:
            return 2


class KiviPaperiSakset(Sanapeli):
    def __init__(self, kierrokset: int):
        super().__init__(kierrokset)

    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        ksp = ['kivi', 'sakset', 'paperi']

        # tarkistetaan väärät sanat
        if pelaaja1_sana not in ksp and pelaaja2_sana not in ksp:
            return 0
        if pelaaja1_sana not in ksp:
            return 2
        if pelaaja2_sana not in ksp:
            return 1

        # tarkistetaan kumpi sana voitti
        if pelaaja1_sana == 'kivi':
            if pelaaja2_sana == 'sakset':
                return 1
            if pelaaja2_sana == 'paperi':
                return 2
        if pelaaja1_sana == 'paperi':
            if pelaaja2_sana == 'kivi':
                return 1
            if pelaaja2_sana == 'sakset':
                return 2
        if pelaaja1_sana == 'sakset':
            if pelaaja2_sana == 'paperi':
                return 1
            if pelaaja2_sana == 'kivi':
                return 2


if __name__ == '__main__':
    p = KiviPaperiSakset(3)
    p.pelaa()
