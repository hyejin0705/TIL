def dfs(idx, E, add, side):
    global S, N, res
    if idx == E:
        if side == 'L':
            if not add in leftNums:
                leftNums[add] = 1
            else:
                leftNums[add] += 1
        elif S - add in leftNums:
            res += leftNums[S - add]
        return

    dfs(idx + 1, E, add + nums[idx], side)
    dfs(idx + 1, E, add, side)


N, S = map(int, input().split())

nums = list(map(int, input().split()))

res = 0

leftNums = {}

# 왼쪽 수열
dfs(0, N // 2, 0, 'L')

# 오른쪽 수열
dfs(N // 2, N, 0, 'R')

if S == 0:
    res -= 1

print(res)