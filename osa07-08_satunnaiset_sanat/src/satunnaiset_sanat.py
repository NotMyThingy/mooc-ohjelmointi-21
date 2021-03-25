from random import sample


def sanat(n: int, alku: str):
    sanalista = []
    with open('sanat.txt') as tiedosto:
        for sana in tiedosto:
            if sana.startswith(alku):
                sanalista.append(sana.strip())

    if len(sanalista) < n:
        raise ValueError('Ei tarpeeksi sopivia')

    return sample(sanalista, n)


if __name__ == '__main__':
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)
