# 10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.

# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.
# 각 테스트 케이스는 첫 줄에 자연수의 개수 N(1 ≤ N ≤ 100)이 주어지고, 그 다음 줄에는 N개의 자연수가 주어진다.
# 각각의 자연수 사이에는 하나씩의 공백이 있다.

import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스의 개수
for _ in range(T):
    N = int(input())  # 자연수의 개수
    print(sum(list(map(int, input().split()))))
