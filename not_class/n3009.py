'''
3009번: 네 번째 점 / bronze 3 / 구현
'''
x, y = map(int, input().split())
a, b = map(int, input().split())
p, q = map(int, input().split())

if x == a:
    res_x = p
elif x == p:
    res_x = a
else:
    res_x = x
if y == b:
    res_y = q
elif y == q:
    res_y = b
else:
    res_y = y
print(res_x, res_y)
