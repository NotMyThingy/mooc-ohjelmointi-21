# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")

indeksi = sana.find(merkki)
if indeksi >= 0 and indeksi + 3 <= len(sana):
    print(sana[indeksi:indeksi + 3])
