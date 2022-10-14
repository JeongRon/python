"""
퀵 정렬 / 일반적인 경우
: 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 평균 시간 복잡도 : O(N logN)
    - 최선의 경우 O(N) ~ 최악의 경우 O(N²)
- 공간 복잡도 : O(N)
- 대부분의 경우에 가장 적합하며, 충분히 빠름
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
