x,y = map(int, input().split())

# ex : 3, 4
# 1 22 333 4444 55555
# 2+3 = 5

a,b=map(int,input().split())
data=[0]
sum=0

for i in range(1,b+1):
  for j in range(i):
    data.append(i)

for i in range(a, b+1):
  sum+=data[i]
print(sum)

# 구글의 도움을 받았읍니다.
# ㅠㅠ