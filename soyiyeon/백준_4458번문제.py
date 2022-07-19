# 4458
# 문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.

N = int(input())  # 줄의 수 입력

for i in range(N):
    s = str(input())
    s = s[0].upper() + s[1:]  # 문장의 첫 번째 글자만 대문자로 바꿔줌.
    print(s)
