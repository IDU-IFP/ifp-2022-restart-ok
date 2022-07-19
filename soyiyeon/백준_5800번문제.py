# 5800
# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다.
# 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.
# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

k = int(input())  # 반의 수

for i in range(k):  # 반의 수 만큼 반복

    a = list(map(int, input().split()))
    del a[0]  # del 예약어 사용해서 0번째 요소 삭제
    a.sort()  # 오름차순으로 리스트 정렬
    diff = []
    print('Class', i+1)
    for i in range(len(a)-1):  # (a의 문자열의 길이를 반환)-1 만큼 반복
        diff.append(a[i+1] - a[i])  # 배열에 요소 추가

    print('Max', str(max(a))+',', 'Min',
          str(min(a))+',', 'Largest gap', max(diff))
