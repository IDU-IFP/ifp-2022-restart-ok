# 1357
# Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자.
# 예를 들어, X=123일 때, Rev(X) = 321이다.
# 그리고, X=100일 때, Rev(X) = 1이다.
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오

def Rev(x):  # Rev()함수 구현, 매개변수로 숫자로 이루어진 문자열 x를 하나 받음
    x = int(x[::-1])  # 문자열 x를 뒤집고 정수형으로 만들어 줌
    return x  # 뒤집어진 정수형 x를 반환


X, Y = input().split(' ')  # X, Y 첫째줄에 입력
result = Rev(str(Rev(X) + Rev(Y)))  # Rev 함수는 문자열 형태의 인수를 받으므로 문자열 형태로 변환해서 넣어줌
print(result)
