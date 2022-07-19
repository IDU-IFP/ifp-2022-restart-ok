# 빠른 A+B

import sys  # sys를 포함. sys.stdin.readline()을 사용할 수 있도록 하는 코드

c = int(input())  # 입력할 갯수 지정
for i in range(c):  # c-1 만큼 반복
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
