# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(koko, merkki):
    if merkki == '':
        merkki = '*'
    print(merkki * koko)


def kuvio(koko, kolmio_merkki, kannan_korkeus, kanta_merkki):
    # tulostetaan kolmio
    merkkien_maara = 1
    while merkkien_maara <= koko:
        viiva(merkkien_maara, kolmio_merkki)
        merkkien_maara += 1

    # tulostetaan kolmion kanta
    korkeus = 0
    while korkeus < kannan_korkeus:
        viiva(koko, kanta_merkki)
        korkeus += 1


if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
