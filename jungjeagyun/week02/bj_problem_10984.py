snum = int(input()) # 학기 수를 입력받는다.
for _ in range(snum): # 입력받은 학기 수만큼 반복하는 것 : 과목 수 입력받고, 과목 수만큼 학점/성적 입력받고, 총 학점과 평점 출력하기
    sumC = finalG = GPA = 0
    objnum = int(input()) # 과목 수 입력받음
    for i in range(objnum):
        c, g = map(float, input().split(' ')) # c에는 학점이, g에는 성적이 입력된다.
        # 해야할 것 : 학점의 총합을 구해야 함
        # 해야할 것 2 : c*g의 합계/ 학점의총합
        sumC = sumC + c
        finalG = finalG + c*g
        GPA = finalG/sumC
    print(f'{int(sumC)} {round(GPA, 1)}')
