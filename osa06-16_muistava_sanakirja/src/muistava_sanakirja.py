# tee ratkaisu tänne
with open('sanakirja.txt') as tiedosto:
    sanakirja = []
    for rivi in tiedosto:
        sanakirja.append(rivi.rstrip())

while True:
    print('1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu')
    valinta = input('Valinta: ')
    if valinta == '1':
        sana_suomeksi = input('Anna sana suomeksi: ')
        sana_englanniksi = input('Anna sana englanniksi: ')
        sanakirja.append(f'{sana_suomeksi} - {sana_englanniksi}')
        print('Sanapari lisätty')
    elif valinta == '2':
        haettu_sana = input('Anna sana: ')
        for sanapari in sanakirja:
            if haettu_sana in sanapari:
                print(sanapari)
    elif valinta == '3':
        break

with open('sanakirja.txt', 'w') as tiedosto:
    for sanapari in sanakirja:
        tiedosto.write(sanapari + '\n')

print('Moi!')
