# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

n = int(input())

li = []
for i in str(n):
    li.append(int(i))
# li = list(map(int,str(n))) 으로 변경가능

li.sort(reverse=True)  # 내림차순

for i in li:
    print(i, end='')
