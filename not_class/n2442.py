'''
2442번: 별 찍기 - 5 / bronze 3 / 구현
'''
n = int(input())
star = [n - 1, n - 1]
for i in range(n):
    for j in range(star[1] + 1):
        if star[0] <= j:
            print("*", end='')
        else:
            print(" ", end='')
    print()
    star[0] -= 1
    star[1] += 1
