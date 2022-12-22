'''
4948번 - 베르트랑 공준 / silver 2 / math.sqrt()
'''
import math


def is_prime(i):
    for num in range(2, int(math.sqrt(i) + 1)):
        if i % num == 0:
            return False
    return True


while True:
    first = int(input())
    if first == 0:
        break
    last = first * 2
    cnt = 0
    for i in range(first + 1, last + 1):
        if is_prime(i):
            cnt += 1
    print(cnt)
