# tee ratkaisu tänne
from string import ascii_lowercase, digits
from random import choice, shuffle


def luo_hyva_salasana(pituus: int, numerot_mukaan: bool, merkit_mukaan: bool):
    salasana = []
    erikoismerkit = '!?=+-()#'
    arvontajoukko = ascii_lowercase

    if numerot_mukaan:
        salasana.append(choice(digits))
        arvontajoukko += digits

    if merkit_mukaan:
        salasana.append(choice(erikoismerkit))
        arvontajoukko += erikoismerkit

    for i in range(pituus - len(salasana)):
        salasana.append(choice(arvontajoukko))

    shuffle(salasana)
    return ''.join(salasana)


if __name__ == '__main__':
    for i in range(10):
        print(luo_hyva_salasana(8, True, True))
