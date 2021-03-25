# tee ratkaisu tänne
from string import ascii_lowercase as ascii
from random import choice


def luo_salasana(pituus: int):
    salasana = ''
    for i in range(pituus):
        salasana += choice(ascii)

    return salasana


if __name__ == '__main__':
    for i in range(10):
        print(luo_salasana(8))
