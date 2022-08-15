"""
2738 - 행렬 덧셈 (bronze 5)
"""
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]
for i in range(N):
    for j in range(M):
        print(C[i][j], end=" ")
    print()
