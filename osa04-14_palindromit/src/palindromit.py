# tee ratkaisu tänne
def palindromi(sana):
    return sana == sana[::-1]


while True:
    sana = input("Anna palindromi: ")
    if palindromi(sana):
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
