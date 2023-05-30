'''
10101번: 삼각형 외우기 / bronze 4 / 구현
'''
num = []
for _ in range(3):
    num.append(int(input()))
if num[0] == 60 and num[1] == 60 and num[2] == 60:
    print('Equilateral')
elif sum(num) == 180:
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
