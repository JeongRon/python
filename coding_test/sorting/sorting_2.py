"""
삽입 정렬
- 평균 시간 복잡도 : O(N²)
- 공간 복잡도 : O(N)
- 선택 정렬과 시간 복잡도 똑같지만,
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면
  매우 빠르게 동작
- 즉, 최선의 경우 O(N)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
