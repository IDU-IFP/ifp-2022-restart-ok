#5543_상근날드
a=[]
b=[]
for _ in range(3):
    a.append(int(input()))
ham = min(a)
for _ in range(2):
    b.append(int(input()))
um = min(b)
print(ham + um -50)