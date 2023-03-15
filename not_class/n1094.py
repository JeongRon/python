'''
1094번: 막대기 / silver 5 / 그리디
'''
x = int(input())
stick = 64
cnt = 0
while x != 0:
    if x < stick:
        stick /= 2
    elif x >= stick:
        x -= stick
        cnt += 1
print(cnt)
