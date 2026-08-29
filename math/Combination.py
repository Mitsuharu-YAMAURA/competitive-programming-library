# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library
def Combination(n, k, mod=998244353):
    top = 1
    bottom = 1

    for i in range(n, n - k, -1):
        top *= i
        top %= mod
    for i in range(k, 0, -1):
        bottom *= i
        bottom %= mod

    nCk = top * pow(bottom, -1, mod)
    return nCk % mod
