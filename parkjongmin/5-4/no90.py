#11655_ROT13
a = input()
b = ''
for c in a:
    if 'a' <= c <= 'z':
        b += chr((ord(c)+13) if c <= 'm' else ord(c)-13)
    elif 'A' <= c <= 'Z':
        b += chr((ord(c)+13) if c <= 'M' else ord(c)-13)
    else:
        b += c
print(b)