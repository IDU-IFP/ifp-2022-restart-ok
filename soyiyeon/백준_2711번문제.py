# 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.
# 창영이는 오타를 반드시 1개만 낸다.

for _ in range(int(input())):
    n, string = input().split()
    n = int(n)
    print(string[:n-1], string[n:], sep='')
