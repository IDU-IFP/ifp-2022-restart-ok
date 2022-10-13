N = int(input())

for i in range(N):
    wrongIndex, wrongStr = input().split()
    wrongIndex = int(wrongIndex)
    wrongList = list(wrongStr)
    del wrongList[wrongIndex-1]
    print(''.join(s for s in wrongList))

