# 11655
# 문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

# re
s = input()
answer = ''
for x in s:
    if 'a' <= x and x <= 'z':
        x = ord(x)+13
        if x > 122:
            x -= 26
        answer += chr(x)
    elif 'A' <= x and x <= 'Z':
        x = ord(x)+13
        if x > 90:
            x -= 26
        answer += chr(x)
    else:
        answer += x

print(answer)
