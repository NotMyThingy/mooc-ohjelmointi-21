# Kirjoita ratkaisu tähän
print("Syötä kokonaislukuja, 0 lopettaa:")

lukuja = 0
summa = 0
positiivisia = 0
while True:
    luku = int(input("Luku: "))

    if luku == 0:
        break

    lukuja += 1
    summa += luku

    if luku > 0:
        positiivisia += 1

print()
print(f"Lukuja yhteensä {lukuja}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa / lukuja}")
print(f"Positiivisia {positiivisia}")
print(f"Negatiivisia {lukuja - positiivisia}")
