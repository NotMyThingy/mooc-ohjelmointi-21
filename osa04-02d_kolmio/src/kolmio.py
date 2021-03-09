# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(maara, merkki):
    if merkki == '':
        merkki = '*'
    print(merkki[0] * maara)


def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    maara = 1
    while maara <= koko:
        viiva(maara, "#")
        maara += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)
