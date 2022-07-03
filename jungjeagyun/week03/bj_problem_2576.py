list = [] # 홀수만 담는 리스트.

for i in range(7):
    a = int(input()) # 7번 입력받음.
    if a%2 != 0: #홀수면 리스트에 저장
        list.append(a)

if list:
    print(sum(list))
    print(min(list))
else:
    print(-1)