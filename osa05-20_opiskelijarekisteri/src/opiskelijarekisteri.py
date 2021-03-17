# tee ratkaisu tänne
def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    if nimi not in opiskelijat:
        opiskelijat[nimi] = {}


def tulosta(opiskelijat: dict, nimi: str):
    if nimi not in opiskelijat:
        print(f'ei löytynyt ketään nimellä {nimi}')
        return

    suoritukset = opiskelijat[nimi]

    print(f'{nimi}:')
    if len(suoritukset) == 0:
        print(' ei suorituksia')
    else:
        print(f' suorituksia {len(suoritukset)} kurssilta:')
        summa = 0
        for kurssi, suoritus in suoritukset.items():
            arvosana = suoritus[1]
            print(f'  {kurssi} {arvosana}')
            summa += arvosana

        print(f' keskiarvo {summa / len(suoritukset):.1f}')


def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    suoritukset = opiskelijat[nimi]
    kurssi, arvosana = suoritus[:]

    # hylättyjä ei kirjata
    if arvosana == 0:
        return

    # jos aiempi arvosana kurssista korkeampi, uutta ei kirjata
    if kurssi in suoritukset and suoritukset[kurssi][1] > arvosana:
        return

    suoritukset[kurssi] = suoritus


def kooste(opiskelijat: dict):
    opiskelijoita = len(opiskelijat)
    eniten_suorituksia = 0
    paras_ka = 0
    for nimi, suoritukset in opiskelijat.items():
        if len(suoritukset) > eniten_suorituksia:
            eniten_suorituksia = len(suoritukset)
            eniten = nimi

        summa = 0
        for kurssi, suoritus in suoritukset.items():
            summa += suoritus[1]

        if summa == 0:
            ka = 0
        else:
            ka = summa / len(suoritukset)

        if ka > paras_ka:
            paras_ka = ka
            paras = nimi

    print(f'opiskelijoita {opiskelijoita}')
    print(f'eniten suorituksia {eniten_suorituksia} {eniten}')
    print(f'paras keskiarvo {paras_ka} {paras}')


def main():
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)


if __name__ == '__main__':
    main()
