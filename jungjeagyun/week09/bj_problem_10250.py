'''
h = 6층, w = 12개의 방을 폭으로 가지는 호텔일 때:

엘리베이터를 타고 이동하는 거리는 신경쓰지 않으므로,
    n=1 101호 -> n=2 201호 -> n=3 301호 -> n=4 401호 -> ... n=6 601호
이후 n=7 102호 -> n=8 202호 -> n=9 302호 -> n=10 402호 -> ... n=12 602호

층수 : N에서 건물 층수를 나눈 나머지
호수 : N에서 건물 층수를 나눈 몫 +1
'''
for _ in range(int(input())):
    height, width, n = map(int, input().split(' '))
    room_num = n // height+1 # 호수
    room_height = n % height
    if n % height == 0:
        room_num = n // height
        room_height = height
    print(f'{room_height * 100 + room_num}')