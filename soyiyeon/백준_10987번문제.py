# 10987
# 알파벳 소문자로만 이루어진 단어가 주어진다.
# 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.

a = input()  # 단어를 입력
v = 'aeiou'  # 변수 v에 모음 선언
ans = 0  # 모음의 개수를 저장할 변수 ans 선언

for i in v:
    ans += a.count(i)  # for문을 돌면서 count() 함수를 사용하여 a에 있는 모음의 개수를 세어 ans에 더함.

print(ans)
