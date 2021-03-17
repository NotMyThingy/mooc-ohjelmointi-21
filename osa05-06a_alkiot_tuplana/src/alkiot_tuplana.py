def tuplaa_alkiot(luvut: list):
    tmp = []
    for alkio in luvut:
        tmp.append(alkio*2)

    return tmp


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
