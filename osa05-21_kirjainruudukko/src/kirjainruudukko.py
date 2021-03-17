# Kirjoita ratkaisu tähän

kerroksia = int(input('Kerrokset: '))

merkit = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


for x in range(-kerroksia + 1, kerroksia):
    for y in range(-kerroksia + 1, kerroksia):
        merkki = max(abs(x), abs(y))
        print(merkit[merkki], end='')
    print()
