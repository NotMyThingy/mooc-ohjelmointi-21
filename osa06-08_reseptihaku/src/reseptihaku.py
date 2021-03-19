# tee ratkaisu tänne
def hae_tiedostosta(tiedosto):
    reseptit = {}
    with open(tiedosto) as t:
        lista = []
        for rivi in t:
            lista.append(rivi.strip())

        while True:
            # Jos listalla vain yksi resepti
            if lista.count('') == 0:
                reseptit[lista[0]] = lista[1:]
                break

            # lisätään resepti sanakirjaan ja poistetaan listalta
            loppu = lista.index('')
            reseptit[lista[0]] = lista[1:loppu]
            lista = lista[loppu + 1:]

    return reseptit


def hae_nimi(tiedosto: str, sana: str):
    loydetyt = []
    reseptit = hae_tiedostosta(tiedosto)
    for resepti in reseptit:
        if sana in resepti.lower():
            loydetyt.append(resepti)

    return loydetyt


def hae_aika(tiedosto: str, aika: int):
    loydetyt = []
    reseptit = hae_tiedostosta(tiedosto)
    for resepti in reseptit:
        if int(reseptit[resepti][0]) <= aika:
            loydetyt.append(
                f'{resepti}, valmistusaika {reseptit[resepti][0]} min')

    return loydetyt


def hae_raakaaine(tiedosto: str, aine: str):
    loydetyt = []
    reseptit = hae_tiedostosta(tiedosto)
    for resepti in reseptit:
        if aine in reseptit[resepti][1:]:
            loydetyt.append(
                f'{resepti}, valmistusaika {reseptit[resepti][0]} min')

    return loydetyt


def main():
    loydetyt = hae_raakaaine("reseptit1.txt", "maito")

    for resepti in loydetyt:
        print(resepti)


if __name__ == '__main__':
    main()
