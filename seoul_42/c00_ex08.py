"""
ft_print_combn
"""


def dfs():
    # 종료 조건
    if arr[0] == 10 - n:
        for i in arr:
            print(i, end="")
    else:
        # 프린트 하기
        while arr[l] < 10:
            for i in arr:
                print(i, end="")
            print(end=", ")
            arr[l] += 1
        # 하나 올리기
        for i in range(l, -1, -1):
            if arr[i] > 10 - n + i:
                arr[i - 1] += 1
                check = i
        # 올린 수 인덱스 오른쪽 애들 오름차순
        for j in range(check, n):
            arr[j] = arr[j - 1] + 1
        # 다시 시작
        dfs()


n = int(input())

arr = [i for i in range(n)]
l = n - 1

dfs()
