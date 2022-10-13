# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

N = int(input())

for j in range(1, N):
    print("*"*(j))

print("*"*N)

for i in range(N-1, 0, -1):
    print("*"*(i))
