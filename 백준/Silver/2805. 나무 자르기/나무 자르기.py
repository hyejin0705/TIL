import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


def binary(arr):
    start = 1
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        m_len = 0
        
        for i in range(n):
            if arr[i] >= mid:
                m_len += arr[i] - mid

        if m_len >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(binary(arr))