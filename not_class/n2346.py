'''
2346번: 풍선 터뜨리기 / silver 3 / 덱
'''
import sys

input = sys.stdin.readline

# 입력받기
N = int(input())
arr = list(map(int, input().split()))

visited = [False for _ in range(N)]
now_index = 0
cnt = 0
while True:
    # 터뜨리기
    print(now_index + 1, end=' ')
    visited[now_index] = True
    cnt += 1
    if cnt == N:
        break
    # 다음 풍선 인덱스 이동
    move = arr[now_index]
    tmp = 0
    if move > 0:
        plus = 1
    else:
        plus = -1
    while tmp != move:
        tmp += plus
        now_index += plus
        if now_index == -1:
            now_index = len(arr) - 1
        elif now_index == len(arr):
            now_index = 0
        while visited[now_index]:
            now_index += plus
            if now_index == -1:
                now_index = len(arr) - 1
            elif now_index == len(arr):
                now_index = 0
