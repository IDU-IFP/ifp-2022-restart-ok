#5576_콘테스트
w=[]
k=[]
for i in range(20):
    n = int(input())
    if i < 10:
        w.append(n)
    else:
        k.append(n)
w.sort()
k.sort()
print(w[7]+w[8]+w[9], k[7]+k[8]+k[9])
