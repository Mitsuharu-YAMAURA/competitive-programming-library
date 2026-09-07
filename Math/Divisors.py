# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library

# 約数列挙を行う
# 計算量は√n


def Divisors(n):
    i = 1
    upper = []
    lower = []
    while i**2 <= n:
        if n % i == 0:
            if n // i != i:
                upper.append(n // i)
            lower.append(i)
    i += 1

    return lower + upper[::-1]
