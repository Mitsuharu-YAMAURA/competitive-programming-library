# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library


def Factorial(n, mod=998244353):
    fact = 1
    for i in range(1, n):
        fact *= i
        fact %= mod

    return fact
