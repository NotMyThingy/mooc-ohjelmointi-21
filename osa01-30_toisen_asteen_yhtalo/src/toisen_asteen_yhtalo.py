# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

a = int(input("Anna a: "))
b = int(input("Anna b: "))
c = int(input("Anna c: "))

x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)

print(f"Juuret ovat {x1} ja {x2}")
