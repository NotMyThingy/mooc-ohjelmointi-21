# tee ratkaisu tänne
def positiivisten_summa(lista):
    summa = 0
    for luku in lista:
        if luku > 0:
            summa += luku

    return summa


if __name__ == '__main__':
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)
