# tee ratkaisu tänne
from random import sample


def heita(noppa: str):
    nopat = {
        'A': [3, 3, 3, 3, 3, 6],
        'B': [2, 2, 2, 5, 5, 5],
        'C': [1, 4, 4, 4, 4, 4]
    }
    return sample(nopat[noppa], 1)[0]


def pelaa(noppa1: str, noppa2: str, kertaa: int):
    n1pisteet = 0
    n2pisteet = 0
    tasapeli = 0

    for i in range(kertaa):
        n1 = heita(noppa1)
        n2 = heita(noppa2)

        if n1 > n2:
            n1pisteet += 1
        elif n2 > n1:
            n2pisteet += 1
        else:
            tasapeli += 1

    return n1pisteet, n2pisteet, tasapeli


if __name__ == '__main__':
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)
