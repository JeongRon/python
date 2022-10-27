"""
<< 서로소 집합 - 경로 압축 >>

- 찾기(find)함수를 호출한 이후에 해당 노드의 루트 노드가 부모 노드가 된다.
- 모든 합집합(Union) 함수를 처리 후, 각 원소에 대하여 찾기(find)함수를 수행하면, 부모 테이블이 갱신
- 기본적인 방법에 비하여 시간 복잡도 개선
"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수, 간선 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력하기
print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
