import sys
 
N = int(sys.stdin.readline())
children = [int(sys.stdin.readline()) for _ in range(N)]
LIS = [0]
length = 0
 
for num in children:
    if num > LIS[-1]:
        LIS.append(num)
        length += 1
    else:
        left = 0
        right = len(LIS)
 
        while left < right:
            mid = (left + right) // 2
 
            if LIS[mid] >= num:
                right = mid
            else:
                left = mid + 1
        
        LIS[right] = num
 
print(N - length)