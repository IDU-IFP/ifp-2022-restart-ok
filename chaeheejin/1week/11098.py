#첼시를 도와줘!
#11098번
n = int(input())

for case in range(n):
    p = int(input())
    max_price = 0
    max_price_player = ''
    
    for player in range(p):
        price, player_name = input().split(' ')

        if max_price < int(price):
            max_price = int(price)
            max_price_player = player_name

print(max_price_player)