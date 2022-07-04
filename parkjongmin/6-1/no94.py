#2941_크로아티아 알파벳
a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
b = input()
for i in a:
    b = b.replace(i,'*')
print(len(b))