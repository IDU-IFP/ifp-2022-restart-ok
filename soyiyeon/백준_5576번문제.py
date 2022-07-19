# 5576
# 두 대학에서 모두 10 명씩이 콘테스트에 참여했다.
# 긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.
# W 대학 및 K 대학 참가자의 점수 데이터가 주어진다. 이때, 각각의 대학의 점수를 계산하는 프로그램을 작성하라.

w = []  # w배열 생성
k = []  # k배열 생성
for i in range(0, 10):
    a = int(input())
    w.append(a)  # w배열에 a로 입력받은 값 추가
for i in range(0, 10):
    b = int(input())
    k.append(b)  # k배열에 b로 입력받은 값 추가
w.sort(reverse=True)  # w배열 내림차순으로 정렬
k.sort(reverse=True)  # k배열 내림차순으로 정렬
wsum = 0
ksum = 0
for i in range(0, 3):
    wsum += w[i]  # w배열의 0번째 인덱스부터 2번째 인덱스에 있는 숫자가 누적해서 wsum에 더해짐.
    ksum += k[i]  # k배열의 0번째 인덱스부터 2번째 인덱스에 있는 숫자가 누적해서 ksum에 더해짐.
print(wsum, ksum)
