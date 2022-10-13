#최대공약수와 최소공배수
#2609
a, b = map(int, input().split())
gcd, lcm = 0, 0

lcm = a * b

if a >= b:
  gcd = a
  a = b
  b = gcd

def func(a, b):
  if a % b == 0: return b
  return func(b, a % b)

gcd = func(a, b)
lcm = lcm // gcd

print(gcd)
print(lcm)