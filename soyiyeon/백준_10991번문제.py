# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())

for i in range((N-1), -1, -1):
    print(" " * i + "* " * (N - i))
