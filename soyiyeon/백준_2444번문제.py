# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

N = int(input())

for j in range(1, N):
    print(" "*(N-j) + "*"*(2*j-1))

print("*"*(2*N-1))

for i in range(N-1, 0, -1):
    print(" "*(N-i) + "*"*(2*i-1))
