# 11047
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())  # 동전 종류수 N, 가치의 합 K

coins = []  # 동전들을 리스트 형태로 입력받기 위해 배열 생성

for i in range(N):  # 동전 종류 수만큼 반복
    coins.append(int(input()))  # 입력받은 동전 종류를 a 리스트에 추가
coins.sort(reverse=True)  # a 리스트를 오름차순으로 정렬

answer = 0  # 최소 동전값 초깃값 0으로 설정
for coin in coins:
    if K >= coin:  # 동전이 가치의 합보다 작거나 같으면
        answer += K // coin  # 가치의 합을 동전으로 나눈 후 정수값만 answer에 저장
        K %= coin  # 가치의 합을 동전으로 나누고 나머지
        if K == 0:  # K가 0이되면 빠져나옴
            break
print(answer)  # 동전 개수 최솟값 출력
