# tee ratkaisu tänne
def pisin_naapurijono(lista):
    pisin = 1
    temp = 1
    for i in range(len(lista)-1):
        if abs(lista[i] - lista[i+1]) == 1:
            temp += 1
        else:
            temp = 1
        pisin = max(pisin, temp)
    return pisin


if __name__ == '__main__':
    lista = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(pisin_naapurijono(lista))
