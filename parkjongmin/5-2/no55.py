#2750_수 계산하기
a = []
for _ in range(int(input())):
    a.append(int(input()))
b = sorted(a)
for i in range(len(a)):
    print(b[i])