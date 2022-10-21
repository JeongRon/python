"""
2448 - 별 찍기 11 / gold 4 / 재귀
"""
n = int(input())

graph = [[" "] * 2 * n for _ in range(n)]


def recursive(x, y, n):
    if n == 3:
        #   *
        graph[x][y] = "*"
        #  * *
        graph[x + 1][y - 1] = "*"
        graph[x + 1][y + 1] = "*"
        # *****
        for i in range(-2, 3):
            graph[x + 2][y + i] = "*"
    else:
        depth = n // 2
        recursive(x, y, depth)
        recursive(x + depth, y - depth, depth)
        recursive(x + depth, y + depth, depth)


recursive(0, n - 1, n)
for i in graph:
    print("".join(i))
