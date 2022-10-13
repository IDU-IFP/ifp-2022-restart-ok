# 하나의 플러그가 있고, N개의 멀티탭이 있다.
# 각 멀티탭은 몇 개의 플러그로 이루어져 있다고 한다.
# 최대 몇 대의 컴퓨터를 전원에 연결할 수 있을까?

# 첫째 줄에 멀티탭의 개수 N이 주어진다. (1 ≤ N ≤ 500,000)
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 각 멀티탭이 몇 개의 플러그를 꽂을 수 있도록 되어 있는지를 나타내는 자연수가 주어진다.

import sys
input = sys.stdin.readline

N = int(input())  # 멀티탭의 갯수

total = 0  # 콘센트를 꽂을 수 있는 갯수
for _ in range(N):
    total += int(input())

print(total - (N - 1))
