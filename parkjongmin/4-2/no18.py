#2443_별 찍기-6
n = int(input())
for i in range(n, 0, -1) :
    print(' '*(n-i), '*'*(i-1), '*', '*'*(i-1), sep='')