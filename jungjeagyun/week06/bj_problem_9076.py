T = int(input())


'''
10 8 5 7 9
5 7 8 9 10
0 1 2 3 4
->7, 9
'''

for _ in range(T):
    case = list(map(int, input().split()))
    case.sort()
    if case[-2] - case[1] >= 4:
        print("KIN")
    else:
        print(case[1]+case[2]+case[3])