#12935_제일 작은 수 제거하기
def solution(a):
    a.pop(a.index(min(a)))
    return a if a else [-1]