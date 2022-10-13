numlist = [0,0,0]

for i in range(3):
    numlist[i] = int(input())

result = str(numlist[0]*numlist[1]*numlist[2])

for k in range(10):
    print(result.count(str(k)))
