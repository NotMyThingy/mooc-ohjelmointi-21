# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")

while True:
    if len(sana) == 0:
        break

    indeksi = sana.find(merkki)
    if indeksi >= 0 and indeksi + 3 <= len(sana):
        print(sana[indeksi:indeksi + 3])
    else:
        break

    sana = sana[indeksi + 1:]
