import random

alphbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getrandom():
    a = random.choice([ 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])
    b = random.randint(1, 25)
    return a, b


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n



def coding():
    string = input('Введите открытый текст:')
    coded_str = ''
#    var = input('Введите 1 если, хотите ввести свой ключ, 2 - если хотите сгенерировать ключ')
    a, b = getrandom()
#    a, b = int(input())
    for i in string:

        coded_str += alphbet[(a * alphbet.index(i) + b) % 26]

    return 'Шифртекст: ' + coded_str, 'Значение а: ' + str(a), 'Значение b: ' + str(b)


def encoding():
    coded_string = input('Введите шифртекст: ')
    a = int(input('Введите значение а: '))
    b = int(input('Введите значение b: '))
    encoded_string = ''
    ai = mulinv(a, 26)
    for i in coded_string:
        encoded_string += alphbet[(ai*(alphbet.index(i) - b)) % 26]
    return encoded_string


print(coding())
