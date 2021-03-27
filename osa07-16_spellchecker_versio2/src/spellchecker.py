# tee ratkaisu tänne
from difflib import get_close_matches as match


def sanakirja():
    with open('wordlist.txt') as tiedosto:
        sanat = []
        for sana in tiedosto:
            sanat.append(sana.strip())
    return sanat


def main():
    sanat = sanakirja()
    teksti = input("Write text: ")
    typot = []
    for sana in teksti.split(' '):
        if sana.lower() in sanat:
            print(f'{sana} ', end='')
        else:
            print(f'*{sana}* ', end='')
            typot.append(sana)

    print('\nKorjausehdotukset:')

    for sana in typot:
        matches = match(sana, sanat, 3)
        print(f'{sana}: {", ".join(matches)}')


main()
