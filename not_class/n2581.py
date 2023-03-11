'''
2581번: 소수 / silver 5 / 소수 판별 
'''


# 소수 판별
def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


# 1. 입력
m = int(input())
n = int(input())
# 2. m~n 사이의 소수 찾기
prime = []
for num in range(m, n + 1):
    if is_prime(num):
        prime.append(num)
# 3. 출력
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
