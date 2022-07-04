#1357_뒤집힌 덧셈
a, b = map(int,input().split())
print(int(str(int(str(a)[::-1]) + int(str(b)[::-1]))[::-1]))