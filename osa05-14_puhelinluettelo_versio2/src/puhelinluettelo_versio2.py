# tee ratkaisu tänne
def hae(puhelinluettelo: dict):
    nimi = input('nimi: ')
    if nimi not in puhelinluettelo:
        print('ei numeroa')
    else:
        for numero in puhelinluettelo[nimi]:
            print(numero)


def lisaa(puhelinluettelo: dict):
    nimi = input('nimi: ')
    numero = input('numero: ')
    if nimi not in puhelinluettelo:
        puhelinluettelo[nimi] = []
    puhelinluettelo[nimi].append(numero)
    print('ok!')


def main():
    puhelinluettelo = {}
    while True:
        komento = input('komento (1 hae, 2 lisää, 3 lopeta): ')
        if komento == '1':
            hae((puhelinluettelo))
        elif komento == '2':
            lisaa(puhelinluettelo)
        elif komento == '3':
            break
    print('lopetetaan...')


main()
