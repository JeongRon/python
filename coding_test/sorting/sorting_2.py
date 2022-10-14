"""
삽입 정렬
: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 평균 시간 복잡도 : O(N²)
- 공간 복잡도 : O(N)
- 선택 정렬과 시간 복잡도 똑같지만,
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면
  매우 빠르게 동작
- 즉, 최선의 경우 O(N)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
