# https://github.com/Mitsuharu-YAMAURA/competitive-programming-library/tree/main/math


# 10進数→n進数への変換
def basen(x, n):
    answer = []
    while x >= n:
        answer.append(x % n)
        x //= n
    if x != 0:
        answer.append(x)
    return answer[::-1]


print(basen(11, 2))
