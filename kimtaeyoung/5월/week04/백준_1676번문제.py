# 팩토리얼 0의 개수

''' 문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
'''

''' 입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
'''

''' 출력
첫째 줄에 구한 0의 개수를 출력한다.
'''

# 풀이


def f(x):
    return (x * f(x-1)) if x else 1


n = str(f(int(input())))[::-1]

for nn in n:
    if int(nn):
        print(n.index(nn))
        break
