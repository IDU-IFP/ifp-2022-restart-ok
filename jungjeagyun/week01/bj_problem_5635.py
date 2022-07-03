# 5635 - 생일

studentNum = int(input())
studentsInfo = [] # 임의의 빈 리스트 생성

for _ in range(studentNum): # 받아온 학생 수만큼 입력받기
    studentInfo = input().split(' ') # [Smith 24 1 2001] 를 입력했다면, studetInfo에 ['Smith','24','1','2001'] 이 담김
    studentInfo[1:] = list(map(int, studentInfo[1:])) # studetInfo에 ['Smith',24,1,2001] 이 담김(정수형으로 변환)
    studentsInfo.append(studentInfo) # studentsInfo에 위에서 만든 것을 집어 넣음

studentsInfo.sort(key=lambda student: (student[3], student[2], student[1]))
# 구글링 함.. sorted ([list 혹은 dic], key = lambda x: [key로 지정하고 싶은 요소]) 출처: https://engineer-mole.tistory.com/94 [매일 꾸준히, 더 깊이]
# [3], [2], [1] -> 년, 월, 일 순서
# key = lambda 에 대한 공부가 더 필요할것 같음.................

# 가장 먼저 있는 사람 : 제일 늙은 사람
# 가장 뒤에 있는 사람 : 제일 어린 사람

print(studentsInfo[-1][0])
print(studentsInfo[0][0])