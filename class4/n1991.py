"""
1991 - 트리 순회 / silver 1 / 트리, 재귀
"""
import sys

input = sys.stdin.readline

tree = {}
N = int(input().rstrip())
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위
def preorder(node):
    if node != ".":
        print(node, end="")
        preorder(tree[node][0])
        preorder(tree[node][1])


# 중위 inorder
def inorder(node):
    if node != ".":
        inorder(tree[node][0])
        print(node, end="")
        inorder(tree[node][1])


# 후위 postorder
def postorder(node):
    if node != ".":
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
