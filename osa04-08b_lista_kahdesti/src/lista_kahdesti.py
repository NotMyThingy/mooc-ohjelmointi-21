# Kirjoita ratkaisu tähän
lista = []
while True:
    luku = int(input('Anna luku: '))
    if luku == 0:
        break

    lista.append(luku)

    print('Lista:', lista)
    print('Järjestettynä:', sorted(lista))

print('Moi!')
