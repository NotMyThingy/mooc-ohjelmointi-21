# Kirjoita ratkaisu tähän
merkkijono = input('Anna merkkijono: ')
osajono = input('Anna osajono: ')
message = 'Osajono ei esiinny merkkijonossa kahdesti.'

ekan_indeksi = merkkijono.find(osajono)
if ekan_indeksi >= 0:
    tokan_indeksi = merkkijono[ekan_indeksi + 1:].find(osajono)
    if tokan_indeksi >= 0:
        message = f'Osajonon toinen esiintymä on kohdassa {tokan_indeksi + ekan_indeksi+1}.'

print(message)
