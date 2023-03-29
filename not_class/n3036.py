'''
3036번: 링 / silver 4 / 최대공약수
'''
import math

# 1. 입력 받기
n = int(input())
ring = list(map(int, input().split()))
# 2. 최대공약수 구한 후, 출력하기
for i in range(1, len(ring)):
    g = math.gcd(ring[0], ring[i])
    print("{}/{}".format(ring[0] // g, ring[i] // g))
