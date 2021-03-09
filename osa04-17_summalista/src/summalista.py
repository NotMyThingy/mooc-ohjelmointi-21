# tee ratkaisu tänne
def summa(l1, l2):
    uusi = []
    for i in range(len(l1)):
        uusi.append(l1[i] + l2[i])

    return uusi


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))  # [8, 10, 12]
