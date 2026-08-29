# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library


# modが素数でk<modの場合
def combination(n, k, mod=998244353):
    if k < 0 or n < k:
        return 0

    k = min(k, n - k)

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


def combination_table(n, mod=998244353):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod

    inv_fact[n] = pow(fact[n], -1, mod)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = (
            inv_fact[i] * i % mod
        )  # ((i-1)!)^(-1)=(i!)^(-1)*iだからかけるだけでいい

    return fact, inv_fact


def calc_combination(n, k, fact, inv_fact, mod=998244353):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod
