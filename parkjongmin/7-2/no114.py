#12933_정수 내림차순으로 배치하기
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    n = "".join(n)
    return int(n)