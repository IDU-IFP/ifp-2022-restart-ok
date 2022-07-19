# 크로아티아 알파벳

# 크로아티아 알파벳을 변경한 것을 넣어둔다.
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()

for i in a:
    b = b.replace(i, '*')  # b를 입력받고, b에 a안에 있는 알파벳을 찾아서 a로 바꿈
print(len(b))  # b의 길이 출력
