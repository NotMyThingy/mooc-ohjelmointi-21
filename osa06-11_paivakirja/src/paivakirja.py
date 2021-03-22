# tee ratkaisu tänne

def kirjoita():
    with open('paivakirja.txt', 'a') as tiedosto:
        merkinta = input('Anna merkintä: ')
        tiedosto.write(f'{merkinta}\n')
        print('Päiväkirja tallennettu')


def lue():
    with open('paivakirja.txt') as tiedosto:
        print('Merkinnät:')
        for rivi in tiedosto:
            print(rivi.strip())


with open('paivakirja.txt', 'a') as tiedosto:
    while True:
        print('1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta')
        valinta = input('Valinta: ')

        if valinta == '0':
            break

        if valinta == '1':
            kirjoita()

        if valinta == '2':
            lue()

    print('Heippa!')
