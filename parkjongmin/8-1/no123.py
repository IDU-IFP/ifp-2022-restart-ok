#12921_소수 찾기
def solution(n) :
    temp = set(range(2, n + 1))
    for i in range(2, n + 1) :
        if i in temp :
            temp -= set(range(2 * i, n + 1, i))
    return len(temp)