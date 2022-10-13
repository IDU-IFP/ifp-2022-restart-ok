# N을 입력받은 뒤, 크기가 N인 도미노 세트에는 점이 몇 개 찍혀 있는지 구하는 프로그램을 작성하시오.

N = int(input())

x = 0
for i in range(0, N + 1):
    for j in range(i, N + 1):
        x += i + j
print(x)
