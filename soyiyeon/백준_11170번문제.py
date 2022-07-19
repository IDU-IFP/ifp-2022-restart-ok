# 11170
# N부터 M까지의 수들을 종이에 적었을 때 종이에 적힌 0들을 세는 프로그램을 작성하라.

x = int(input())
for i in range(x):
    count = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        w = str(i)  # 문자열로 변환
        count += w.count('0')  # 0의 개수 셈
    print(count)
