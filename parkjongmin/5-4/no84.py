#10808_알파벳 개수
a=input()
b=[0]*26
for i in a:
    b[ord(i)-97]+=1
print(*b)