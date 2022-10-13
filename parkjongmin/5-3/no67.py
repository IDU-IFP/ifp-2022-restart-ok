#10809_알파벳 찾기
word = input()
a = list(range(97,123))
for x in a :
    print(word.find(chr(x))) 