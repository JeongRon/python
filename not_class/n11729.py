'''
11729번: 하노이 탑 이동 순서 / silver 1 / 재귀
'''


def hanoi(n, start, end):
    if n == 1:
        print(start, end)
    else:
        mid = 6 - start - end
        hanoi(n - 1, start, mid)
        print(start, end)
        hanoi(n - 1, mid, end)


n = int(input())
print(2**n - 1)
hanoi(n, 1, 3)
