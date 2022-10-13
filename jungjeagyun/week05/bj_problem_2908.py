a, b = input().split(' ')
list_a, list_b = list(a), list(b)
list_a.reverse()
list_b.reverse()
reversed_a, reversed_b = int(''.join(list_a)), int(''.join(list_b))

if reversed_a>reversed_b:
    print(reversed_a)
else:
    print(reversed_b)