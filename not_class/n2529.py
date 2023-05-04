'''
2529번: 부등호 / silver 1 / 백트래킹, 브루트포스
'''


def dfs(num, depth):
    # 종료조건
    if depth == k:
        all_case.append(num)
        return
    if inequality[depth] == '>':
        for i in range(10):
            if i in remain and int(num[-1]) > i:
                remain.remove(i)
                dfs(num + str(i), depth + 1)
                remain.add(i)
    if inequality[depth] == '<':
        for i in range(10):
            if i in remain and int(num[-1]) < i:
                remain.remove(i)
                dfs(num + str(i), depth + 1)
                remain.add(i)


# 부등호 개수 k, 부등호 inequality 입력받기
k = int(input())
inequality = list(map(str, input().split()))
# 모든 가능한 숫자 구하기
all_case = []
for v in range(10):
    remain = set(i for i in range(10))
    remain.remove(v)
    dfs(str(v), 0)
# 최대값, 최소값 출력
print(all_case[-1])
print(all_case[0])
