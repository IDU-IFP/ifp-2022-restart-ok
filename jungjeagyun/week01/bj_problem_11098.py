# 11098 - 첼시를 도와줘!!

testCaseNum = int(input())

for _ in range(testCaseNum): # testCaseNum만큼 아래의 테스트 케이스가 반복된다.
    # 테스트 케이스 하나당 하나의 선수 이름이 나와야 함

    playerNum = int(input()) # 선수의 수를 입력받고..

    maxPlayerPrice = 0
    maxPlayerName = ""  # 최종적으로 이것이 결과가 되어야 함

    for _ in range(playerNum): # 선수의 수만큼 검사를 반복
        playerPrice, playerName = input().split(' ') # 이름과 가격을 담고..
        playerPrice = int(playerPrice) # 가격을 정수형으로 바꿔줌
        if playerPrice>maxPlayerPrice:
            maxPlayerPrice = playerPrice
            maxPlayerName = playerName # 가장 비싼 선수를 정함
    print(maxPlayerName)