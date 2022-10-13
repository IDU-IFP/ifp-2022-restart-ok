#10987_모음의 개수
n=str(input())
c=0
if n.count('a') or n.count('e') or n.count('i') or n.count('o') or n.count('u'):
    c = c + ((c + n.count('a')) + (c +  n.count('e')) + (c +  n.count('i')) +
    (c +  n.count('o')) +(c +  n.count('u')))
print(c)