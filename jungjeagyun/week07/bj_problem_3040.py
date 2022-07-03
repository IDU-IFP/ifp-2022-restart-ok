# 아이디어 : 모든 숫자의 합에서 2개의 숫자를 빼면 100이 됨
# 구글링의 힘. 이거랑 10890 빼곤 다 제가 했어요.. 죄송ㅜㅜ
li = sorted([int(input()) for _ in range(9)])
fin = 0
for i in range(8):
    if fin:
        break
    for j in range(i+1, 9):
        if sum(li)-li[i]-li[j] == 100:
            li.pop(j); li.pop(i)
            fin = 1
            break
for n in li:
    print(n)