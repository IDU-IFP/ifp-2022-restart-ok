# 11365
# 당신은 길을 가다가 이상한 쪽지를 발견했다.
# 그 쪽지에는 암호가 적혀 있었는데, 똑똑한 당신은 암호가 뒤집으면 해독된다는 것을 발견했다.
# 이 암호를 해독하는 프로그램을 작성하시오.

while True:  # 무한 반복
    a = input()  # a에 암호 입력받음
    if a == 'END':  # a가 END라면
        break  # while문 빠져나옴
    print(a[::-1])  # 문자열 뒤집어서 출력
