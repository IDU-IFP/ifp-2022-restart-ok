# 3040
# 아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오. (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)

li = sorted([int(input()) for _ in range(9)])
fin = 0
for i in range(8):
    if fin:
        break
    for j in range(i+1, 9):
        if sum(li)-li[i]-li[j] == 100:
            li.pop(j)
            li.pop(i)
            fin = 1
            break
for n in li:
    print(n)
