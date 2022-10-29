"""
5639 - 이진 검색 트리 / gold 4 / 재귀, 트리
"""
import sys

sys.setrecursionlimit(10**9)
preorder = []

while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break


def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if preorder[i] > preorder[start]:
            mid = i
            break
    postorder(start + 1, mid - 1)  # 왼쪽 트리
    postorder(mid, end)  # 오른쪽 트리
    print(preorder[start])  # 루트 노드


postorder(0, len(preorder) - 1)
