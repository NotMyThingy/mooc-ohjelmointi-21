# tee ratkaisu tänne
def uniikit(lista):
    uusi = []
    for luku in lista:
        if luku not in uusi:
            uusi.append(luku)

    return sorted(uusi)


if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))  # [1, 2, 3]
