testCaseNum = int(input())

for _ in range(testCaseNum):
    carPrice = int(input()) # 자동차의 가격 제공하기
    optionsNum = int(input())
    optionsSum = 0 # 초기화
    for i in range(optionsNum): # 옵션의 종류만큼 입력받음
        q, p = map(int, input().split(' ')) # q:옵션의 갯수, p:해당 옵션의 가격
        optionsSum = optionsSum + q*p
    print(optionsSum + carPrice)

