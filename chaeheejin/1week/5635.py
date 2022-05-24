#생일
#5635
n = int(input())
students = []

for student_index in range(n):
    student = input().split(' ')

    #생일 정보인 dd mm yyyy를 정수형으로 변환
    student[1:] = map(int, student[1:])

    #한 학생의 정보를 students 리스트 변수에 넣음
    students.append(student)

    students.sort(key=lambda student: (student[3], student[2], student[1]))
    #나이가 제일 적은사람 이름 출력
    print(students[-1][0])
    #나이가 제일 많은사람 이름 출력
    print(students[0][0])
