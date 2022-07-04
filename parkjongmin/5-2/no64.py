#5176_대회 자리
for _ in range(int(input())) :
  p, m = map(int, input().split())
  d = [0] * (m + 1)
  c = 0
  for _ in range(p) :
    value = int(input())
    if d[value] == 0 :
      d[value] = 1
    else :
      c += 1
  print(c)