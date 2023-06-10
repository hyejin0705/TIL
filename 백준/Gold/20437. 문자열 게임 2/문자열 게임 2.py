def check(txt):
    D = {}
    l = len(txt)
    for i in range(l):
        t = txt[i]
        if not D.get(t, []):
            D[t] = []
        D[t].append(i)
    return D

def check_length(D, K):
    ret = [1e5, 0]
    for arr in D.values():
        l = len(arr)
        if l < K: continue
        for i in range(l-K+1):
            gap = arr[i+K-1]-arr[i]+1
            if ret[0] > gap: ret[0] = gap
            if ret[1] < gap: ret[1] = gap

    return [-1] if ret == [1e5, 0] else ret

T = int(input())
for _ in range(T):
    txt = input()
    K = int(input())
    D = check(txt)
    ret = check_length(D, K)
    print(*ret)