#11098_첼시를 도와줘!
n = int(input())
for _ in range(n) :
  p = int(input())
  ex = 0
  ex_name = ""
  for _ in range(p) :
    price, name = input().split()
    if int(price) > ex :
      ex = int(price)
      ex_name = name
  
  print(ex_name)