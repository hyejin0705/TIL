N, K = map(int, input().split())
numbers = list(map(int, input().split()))

ptr1, ptr2 = 0, 0
cnt, ans, dist = 0, 0, 0

while ptr1 != N and ptr2 != N:
    if numbers[ptr1] % 2:
        if cnt > 0:
            ptr1 += 1
            cnt -= 1
        else:
            ptr1 += 1
            ptr2 = max(ptr1, ptr2)
    else:
        if numbers[ptr2] % 2:
            if cnt >= K:
                if not numbers[ptr1] % 2:
                    dist -= 1
                ptr1 += 1

            else:
                cnt += 1
                ptr2 += 1
                
        else:
            dist += 1
            ptr2 += 1
            
    ans = max(ans, dist)

print(ans)