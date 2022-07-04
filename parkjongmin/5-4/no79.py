#4458_첫 글자를 대문자로
for _ in range(int(input())):
     a = input()
     b = a[0].upper()
     c = b + a[1:]
     print(c)