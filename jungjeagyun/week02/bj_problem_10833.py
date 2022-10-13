# 정수 schoolNum를 입력받음
# schoolNum 만큼 학교의 학생수와 사과갯수를 나타내는 정수를 입력받음
# 남는 사과를 나머지 변수에 담음

schoolNum = int(input())
remainAppleNum = 0

for i in range(schoolNum): # 학교 수만큼 반복한다.
    studentsNum, appleNum = map(int, input().split(' '))
    remainAppleNum = remainAppleNum + appleNum % studentsNum
print(remainAppleNum)