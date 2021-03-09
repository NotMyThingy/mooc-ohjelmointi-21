# Kirjoita ratkaisu tähän
merkkijono = input("Anna merkkijono: ")
alku = len(merkkijono) - 1
while alku >= 0:
    print(merkkijono[alku:])
    alku -= 1
