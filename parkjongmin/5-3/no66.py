#3040_백설 공주와 일곱 난쟁이
t=[]
for _ in range(9):
    t.append(int(input()))
t_sum=sum(t)
a=0
b=0
for i in range(8):
    for j in range(i+1,9):
        if t_sum - (t[i] + t[j]) == 100:
            a = t[i]
            b = t[j]
t.remove(a)
t.remove(b)
for i in t:
    print(i)