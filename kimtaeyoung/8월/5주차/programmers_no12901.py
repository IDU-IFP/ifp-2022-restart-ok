# 2016년

''' 문제 설명
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
'''

# 풀이

import datetime as dt


def solution(a, b):
    day = {0: 'MON', 1: 'TUE', 2: 'WED',
           3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}
    x = dt.datetime(2016, a, b)
    return day[x.weekday()]
