
alphbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a_values = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
b_values = [i for i in range(0, 26)]

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


def encoding():
    coded_string = input('Введите шифртекст: ')
    encoded_string = ''
    for a in a_values:
        ai = mulinv(a, 26)
        for b in b_values:
            for index, i in enumerate(coded_string):
                encoded_string += alphbet[(ai*(alphbet.index(i) + (len(alphbet) - 1) - b)) % 26]
                if index == len(coded_string) - 1:
                    encoded_string += '\n'
    return encoded_string


print(encoding())
