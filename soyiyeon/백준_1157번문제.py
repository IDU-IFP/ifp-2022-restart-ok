# 1157
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

word = input().upper()  # 전체문자를 대문자로 변환하여 변수에 저장
word_list = list(set(word))  # set함수를 사용하여 중복된 문자값 제거 후 변수에 저장

cnt = []
for i in word_list:
    count = word.count
    cnt.append(count(i))  # 알파벳이 사용된 횟수를 리스트에 추가

if cnt.count(max(cnt)) > 1:
    print("?")

else:  # 최댓값이 하나일 때
    # 숫자 리스트 중 가장 큰 수의 위치를 index로 찾아 인덱스에 위치한 문자열 출력
    print(word_list[(cnt.index(max(cnt)))])
