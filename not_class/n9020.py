'''
9020번: 골드바흐의 추측 / silver 2 / 구현
'''


def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


# 0. 소수 세트 만들기
prime = {2, 3}
for i in range(4, 10001):
    if i % 2 == 0:
        continue
    else:
        if is_prime(i):
            prime.add(i)

# 1. 입력 받기
t = int(input())
for _ in range(t):
    n = int(input())
    # 2. 골드바흐 파티션 출력하기
    if n == 4:
        print(2, 2)
    else:
        # 2-1. 골드바흐 파티션 경우의 수 찾아서 possible 리스트에 담기
        possible = []
        for v in prime:
            tmp = n - v
            if tmp in prime:
                possible.append((v, tmp))
        # 2-2. 골드바흐 파티션 중의 두 소수의 차이가 가장 작은 것 출력
        min_gap = 10000
        res_x = 0
        res_y = 0
        for x, y in possible:
            if x <= y and min_gap > y - x:
                min_gap = y - x
                res_x = x
                res_y = y
        print(res_x, res_y)
