"""
음료수 얼려 먹기

1. N * M 의 얼음 틀
2. 얼음 틀의 형태 입력 주어진다
3. 구멍 뚫려있는 부분 1, 음료 들어가 있는 부분 0
4. 한 번에 만들 수 있는 아이스크림 개수 출력
"""


def dfs(x, y):
    # 종료 조건
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice_box[x][y] == 0:
        ice_box[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
ice_box = []
for _ in range(n):
    ice_box.append(list(map(int, input())))

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 1:
            count += 1

print(count)
