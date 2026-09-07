# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library


# 特定の階乗を計算
def factorial(n, mod=998244353):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i % mod

    return fact


# 1からnまでの階乗をすべて前計算
def factorial_table(n, mod=998244353):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod

    return fact
