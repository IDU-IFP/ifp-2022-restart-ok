word = input()
alphabet = list(range(97,123))
# 구글링...
# 아스키코드 숫자 범위를 만드는 건 상상도 못 했음

for x in alphabet :
    print(word.find(chr(x))) 