# def fib():
#     n, m = int(input()), int(input())
#     if n == 1:
#         return 1
#     for i  in range(2, n+1):
#         a, b = 0, 1
#         a, b = b, (a+b)
#         if i == m:
#             f_m = b
#     f_n = b
#
#     if f_n // f_m == 1:
#         return 1
#     elif f_n // f_m > 1:
#         ost = f_n // f_m
#         return f_n - (ost * f_m)
# print(fib())


import random





def test(gcd, n_inter=100):
        for i in range(n_inter):
            c = random.randint(0, 1024)
            a = c * random.randint(0, 128)
            b = c * random.randint(0, 128)

            assert gcd(a, a) == gcd(a, 0) == a
            assert gcd(b, b) == gcd(b, 0) == b
            assert gcd(a, 1) == gcd(b, 1) == 1
            d = gcd(a, b)
            assert a % d == b % d == 0

def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(1, max(1, b) + 1)):
        if d == 0 % d == b % d == 0:
            return d

def gcd2(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)





def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)

    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)


def gcd4(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    print(f'a = {a}, b = {b}')
    return gcd4(b % a, a)


print(gcd4(24, 9))