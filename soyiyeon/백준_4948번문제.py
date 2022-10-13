# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

import sys

n_max = 123456
is_prime = [True] * (2 * n_max + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int((2 * n_max) ** 0.5) + 1):
    if is_prime[i]:
        j = 2
        while (i * j) <= (2 * n_max):
            is_prime[i * j] = False
            j += 1

while (n := int(sys.stdin.readline())) != 0:
    print(is_prime[n + 1:(2 * n) + 1].count(True))
