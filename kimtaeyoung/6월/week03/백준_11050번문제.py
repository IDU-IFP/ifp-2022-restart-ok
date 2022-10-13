# 이항 계수 1

''' 문제
자연수 N과 정수 K가 주어졌을 때 이항 계수 (NK)를 구하는 프로그램을 작성하시오.
'''

''' 입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
'''

''' 출력
(NK)를 출력한다.
'''

# 풀이


def f(x):
    if x:
        return x * f(x-1)
    else:
        return 1


n, k = map(int, input().split())
print(f(n) // f(n-k) // f(k))
