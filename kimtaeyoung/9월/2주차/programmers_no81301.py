# 숫자 문자열과 영단어

''' 문제 설명
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(s):
    engNum = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for word, number in engNum.items():
        s = s.replace(word, str(number))
    return int(s)
