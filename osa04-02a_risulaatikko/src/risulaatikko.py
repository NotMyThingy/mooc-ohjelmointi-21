# kopioi edellisestä tehtävästä funktion viiva koodi tänne

def viiva(leveys, mjono):
    if mjono == '':
        mjono = '*'

    print(leveys * mjono[0])


def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    while korkeus > 0:
        viiva(10, "#")
        korkeus -= 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
