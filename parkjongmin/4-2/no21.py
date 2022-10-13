#2523_별 찍기-13
n = int(input())
for i in range(1, n) :
    print('*', '*'*(i-1), ' '*(n-i), sep='')
for i in range(n, 0, -1) :
    print('*', '*'*(i-1), ' '*(n-i), sep='')
