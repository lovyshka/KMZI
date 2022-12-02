import random

alphbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getrandom():
    a1 = random.choice([3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])
    b1 = random.randint(2, 10)
    a2 = random.choice([3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])
    b2 = random.randint(2, 10)
    # a1 = 3
    # b1 = 10
    # a2 = 5
    # b2 = 4
    return a1, b1, a2, b2


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def coding():
    string = input('Введите открытый текст:').upper()
    coded_string = ''
    keys = getrandom()
    print('Ваши ключи:', keys)
    for index, i in enumerate(string):
        if index == 0:
            coded_string += alphbet[((keys[-4] * alphbet.index(i)) % 26 + keys[-3]) % 26]
        elif index == 1:
            coded_string += alphbet[((keys[-2] * alphbet.index(i)) % 26 + keys[-1]) % 26]
        else:
            ai = (int(keys[-4]) * int(keys[-2])) % 26
            bi = (int(keys[-3]) + int(keys[-1])) % 26
            keys += ai, bi
            coded_string += alphbet[((keys[-2] * alphbet.index(i)) % 26 + keys[-1]) % 26]
            if i == len(string):
                continue
    return coded_string


def encoding():
    string = input('Введите шифртекст:').upper()
    decoded_string = ''
    arr = input('Введите ключи:')
    keys = list(map(int, arr.split(' ')))
    for index, i in enumerate(string):
        if index == 0:
            a_reverse = mulinv(keys[-4], 26)
            decoded_string += alphbet[((alphbet.index(i) - keys[-3]) * a_reverse) % 26]
        elif index == 1:
            a_reverse = mulinv(keys[-2], 26)
            decoded_string += alphbet[((alphbet.index(i) - keys[-1]) * a_reverse) % 26]
        else:
            ai = (int(keys[-4]) * int(keys[-2])) % 26
            bi = (int(keys[-3]) + int(keys[-1])) % 26
            keys += ai, bi
            a_reverse = mulinv(keys[-2], 26)
            decoded_string += alphbet[((alphbet.index(i) - keys[-1]) * a_reverse) % 26]
            if i == len(string):
                continue

    return decoded_string


print(encoding())

