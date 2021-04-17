def alkuluvut():
    luku = 2
    while True:
        if alkuluku(luku):
            yield luku
        luku += 1


def alkuluku(luku):
    for i in range(2, luku):
        if luku % i == 0:
            return False
    return True


if __name__ == "__main__":
    luvut = alkuluvut()
    for i in range(8):
        print(next(luvut))
