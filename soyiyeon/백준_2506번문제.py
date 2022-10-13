# 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다.
# 틀린 문제는 0점으로 계산한다.
# 시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오.

# 첫째 줄에 문제의 개수 N (1 ≤ N ≤ 100)이 주어진다.
# 둘째 줄에는 N개 문제의 채점 결과를 나타내는 0 혹은 1이 빈 칸을 사이에 두고 주어진다.
# 0은 문제의 답이 틀린 경우이고, 1은 문제의 답이 맞는 경우이다.

import sys
input = sys.stdin.readline

N = int(input())  # 문제의 개수
R = list(map(int, input().split()))  # 채점 결과

score = 1
tscore = 0  # 총 점수

for i in range(N):
    if R[i] == 1:
        tscore += score
        score += 1

    if R[i] == 0:
        score = 1

print(tscore)
