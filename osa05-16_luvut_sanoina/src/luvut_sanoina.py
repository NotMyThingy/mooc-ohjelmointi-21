# tee ratkaisu tänne
def lukukirja():
    ykkoset = {
        0: 'nolla', 1: 'yksi', 2: 'kaksi', 3: 'kolme',
        4: 'neljä', 5: 'viisi', 6: 'kuusi', 7: 'seitsemän',
        8: 'kahdeksan', 9: 'yhdeksän'}

    luvut = {}

    # 0 - 9
    for i in range(10):
        luvut[i] = ykkoset[i]

    # erikoistapaus 10
    luvut[10] = 'kymmenen'

    # 11 - 19
    for i in range(1, 10):
        luvut[i + 10] = ykkoset[i] + 'toista'

    # 20 - 99
    for i in range(2, 10):
        luvut[i * 10] = ykkoset[i] + 'kymmentä'
        for j in range(1, 10):
            luvut[i * 10 + j] = ykkoset[i] + 'kymmentä' + ykkoset[j]

    return luvut


def main():
    ykkoset = lukukirja()
    print(ykkoset[2])
    print(ykkoset[11])
    print(ykkoset[45])
    print(ykkoset[99])
    print(ykkoset[0])


if __name__ == '__main__':
    main()
