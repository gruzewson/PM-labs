def zad1():
    M = pow(2, 31)
    a = 69069
    c = 1
    X = 15
    n = 1e5
    numbers = []
    for _ in range(int(n)):
        X = (a*X + c) % M
        numbers.append(X/M)

    section = [0] * 10
    for number in numbers:
        section[int(number * 10)] += 1

    print("zad1: ")
    print(section)

def toNumber(bits):
    number = 0
    for i in range(31):
        if bits[i] == 1:
            number += pow(2, i)
    return number

def zad2():
    p = 7
    q = 3
    b = [1, 0, 0, 1, 1, 0, 1]
    i = len(b)
    n = 1e5
    bits = 31
    max_value = pow(2, 31)
    numbers = []

    for k in range(int(n)):
        i = len(b)
        while i < bits:
            b.append(b[i - p] ^ b[i - q])
            i += 1
        numbers.append(toNumber(b))
        b = b[-7:]

    section = [0] * 10
    for number in numbers:
        section[int(number/max_value * 10)] += 1

    print("\nzad2: ")
    print(section)

zad1()
zad2()