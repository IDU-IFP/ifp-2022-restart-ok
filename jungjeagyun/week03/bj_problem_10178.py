caseNum = int(input())

for i in range(caseNum):
    candies, children = map(int, input().split(' '))
    print(f'You get {candies//children} piece(s) and your dad gets {candies%children} piece(s).')
