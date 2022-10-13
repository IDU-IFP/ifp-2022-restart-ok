word = list(str(input()))
result = list()
for w in word:
    if w.isupper() == True:
        w = w.lower()
        result.append(w)
    else:
        w = w.upper()
        result.append(w)
print(''.join(result))

