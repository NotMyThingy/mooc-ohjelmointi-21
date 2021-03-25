# tee ratkaisu tänne
from random import sample


def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numerot = list(range(alaraja, ylaraja + 1))
    arvotut = sample(numerot, maara)

    return sorted(arvotut)


if __name__ == '__main__':
    for numero in lottonumerot(7, 1, 40):
        print(numero)
