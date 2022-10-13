lineNum = int(input())
# ex : 5

'''
공백의 갯수 : 0 -> 1 -> 2 -> 3, 시작:0, 공차:1
별의 갯수 : 시작:lineNum*2-1, 공차:2
등차수열의 일반항 -> 첫번째수 + (n-1)공차
'''

for i in range(1, lineNum+1):
    print(" "*(i-1)   +   "*"*( (lineNum*2-1)+(i-1)*-2))