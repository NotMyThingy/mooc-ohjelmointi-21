# Kirjoita ratkaisu tähän
sana = input('Sana: ')
if len(sana) % 2 != 0:
    sana += ' '
vali = ' '
tyhjia = (28 - len(sana)) // 2

print('*' * 30)
print('*' + vali * tyhjia + sana + vali * tyhjia + '*')
print('*' * 30)
