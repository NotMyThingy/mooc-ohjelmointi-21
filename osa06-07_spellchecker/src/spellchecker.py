# tee ratkaisu tänne
def sanakirja():
    sanat = []
    with open('wordlist.txt') as tiedosto:
        for sana in tiedosto:
            sanat.append(sana.strip())
    return sanat


def main():
    sanat = sanakirja()
    teksti = input("Write text: ")
    for sana in teksti.split(' '):
        if sana.lower() in sanat:
            print(f'{sana} ', end='')
        else:
            print(f'*{sana}* ', end='')
    print()


if __name__ == '__main__':
    main()
