# tee ratkaisu tänne
from string import whitespace as wspace, ascii_letters as kirjaimet, digits as numerot


def vaihda_koko(merkkijono: str):
    mjono = ''
    for merkki in merkkijono:
        if merkki.isupper():
            merkki = merkki.lower()
        elif merkki.islower():
            merkki = merkki.upper()
        mjono += merkki

    return mjono


def puolita(merkkijono: str):
    keskihohta = len(merkkijono) // 2
    alku = merkkijono[:keskihohta]
    loppu = merkkijono[keskihohta:]

    return alku, loppu


def poista_erikoismerkit(merkkijono: str):
    sallitut = kirjaimet + numerot + wspace + 'äöå'
    mjono = ''
    for merkki in merkkijono:
        if merkki in sallitut:
            mjono += merkki

    return mjono


if __name__ == '__main__':
    mjono = "Moi kaikki!"

    print(vaihda_koko(mjono))

    p1, p2 = puolita(mjono)
    print(p1)
    print(p2)

    m2 = poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
    print(m2)
