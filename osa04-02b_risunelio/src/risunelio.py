# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkki):
    if merkki == '':
        merkki = '*'

    print(merkki * leveys)


def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    korkeus = 0
    while korkeus < koko:
        viiva(koko, "#")
        korkeus += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
