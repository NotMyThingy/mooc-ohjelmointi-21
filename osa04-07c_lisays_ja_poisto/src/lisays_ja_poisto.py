# Kirjoita ratkaisu tähän
lista = []
while True:
    print(f'Lista on nyt {lista}')
    valinta = input('(l)isää, (p)oista vai e(x)it: ')
    if valinta == 'x':
        break

    if valinta == 'l':
        lista.append(len(lista) + 1)

    if valinta == 'p':
        if len(lista) == 0:
            continue
        lista.pop(len(lista) - 1)

print('Moi!')
