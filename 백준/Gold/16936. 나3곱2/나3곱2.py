n = int(input())
array = list(map(int,input().split()))
cnt = 1
total = []
while len(total) != n:
    array2 = []
    total2 = []
    for i in range(len(array)):
        if array[i]%2 == 1:
            total2.append(array[i]*(2**(cnt-1)))
            array[i] = 0
        else:
            array2.append(array[i])

    array = array2[:]
    for i in range(len(array)):
        array[i] = array[i]//2
    cnt += 1
    total2.sort(reverse=True)
    for i in total2:
        total.append(i)

print(*total)