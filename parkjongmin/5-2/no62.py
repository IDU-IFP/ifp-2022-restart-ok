#9076_점수 집계
x = int(input())
for i in range(x):
    a = list(map(int, input().split()))
    a.remove(max(a))
    a.remove(min(a))
    if max(a) - min(a) >= 4:
        print('KIN')
    else:
        print(sum(a))