# 소인수분해
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

N = int(input())
m = 2
while N != 1:  # N과m을 나눴을때 몫이 1이 되면 멈춤.
    if N % m == 0:
        print(m)
        N = N//m
    else:
        m += 1
