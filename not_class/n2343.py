'''
2343번: 기타 레슨 / silver 1 / 이분탐색
'''

n, m = map(int, input().split())
video = list(map(int, input().split()))

# start : video 리스트에서 가장 큰 값
# end : video 리스트 값들을 모두 합한 값
# res : 알맞은 mid의 값 중, 가장 작은 값을 넣을 변수
start = max(video)
end = sum(video)
res = sum(video)

while start <= end:
    # mid : 블루레이 크기 지정
    mid = (start + end) // 2
    # stack_ray : 블루레이 담을 변수, cnt : 블루레이 개수
    stack_ray = 0
    cnt = 1
    # 블루레이 크기가 mid 일때, 블루레이 개수 cnt 구하기
    for i in range(len(video)):
        if stack_ray + video[i] <= mid:
            stack_ray += video[i]
        else:
            cnt += 1
            stack_ray = video[i]
    # cnt 가 m 보다 작거나 같으면, 블루레이 크기(mid) 감소
    # cnt 가 m 보다 크면, 블루레이 크기(mid) 증가
    if cnt <= m:
        end = mid - 1
        res = min(res, mid)
    else :
        start = mid + 1

print(res)
