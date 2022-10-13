#12934_정수 제곱근 판별
def solution(n):
    a = n ** (1/2)
    if a % 1 == 0:
        return (a + 1)** 2
    return -1