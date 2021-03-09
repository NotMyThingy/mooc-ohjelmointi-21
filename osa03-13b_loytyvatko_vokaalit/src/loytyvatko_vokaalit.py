# Kirjoita ratkaisu tähän
merkkijono = input("Anna merkkijono: ")
vokaalit = ['a', 'e', 'o']

for vokaali in vokaalit:
    if vokaali in merkkijono:
        print(f'{vokaali} löytyy')
    else:
        print(f'{vokaali} ei löydy')
