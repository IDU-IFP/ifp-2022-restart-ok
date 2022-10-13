#12916_문자열 내 p와 y의 개수
def solution(s):
    a=s.upper()
    if a.count('P')==a.count('Y'):
        return True
    return False