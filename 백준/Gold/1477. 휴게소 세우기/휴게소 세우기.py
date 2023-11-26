from sys import stdin
n, m, l = map(int, stdin.readline().split())

arr = list(map(int, stdin.readline().split()))
arr.append(0)
arr.append(l)
arr.sort()  # 휴게소 위치 순 정렬

start, end = 1, l
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, len(arr)):
        if (arr[i] - arr[i - 1]) > mid:
            cnt += (arr[i] - arr[i - 1] - 1) // mid  # 같은 자리 설치 불가
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        rst = mid  # while문 중단 시, 답 도출 위함

print(rst)