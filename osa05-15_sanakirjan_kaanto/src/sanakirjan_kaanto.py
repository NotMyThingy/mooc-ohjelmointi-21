# tee ratkaisu tänne
def kaanna(sanakirja: dict):
    temp = {}
    for avain in sanakirja:
        temp[sanakirja[avain]] = avain

    sanakirja.clear()
    for avain in temp:
        sanakirja[avain] = temp[avain]


def main():
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)


if __name__ == '__main__':
    main()
