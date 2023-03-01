# 분할하지 않으면, 수열의 길이가 40이기 때문에,
# 모든 경우의 수가 2 ** 40으로 시간초과 걸림.

# 해결방안 >>> 왼쪽, 오른쪽 나누어서 탐색

# dfs 함수를 활용하는 건 똑같음.
def dfs(idx, E, add, side):
    global S, N, ans
    if idx == E:       # 종료조건
        if side == 'L':              # 왼쪽 수열일때,
            if add not in leftNums:  # 없다면,
                leftNums[add] = 1    # 생성
            else:                    # 있다면,
                leftNums[add] += 1   # 1 증가

        # 목표 - 왼쪽 합 = 오른쪽 합
        elif S - add in leftNums:     # 오른쪽 수열일 때, 확인하기
            ans += leftNums[S - add]

        return

    dfs(idx + 1, E, add + nums[idx], side)
    dfs(idx + 1, E, add, side)


# N: 수열의 개수, S: 목표 합
N, S = map(int, input().split())

# 수열 리스트
nums = list(map(int, input().split()))

ans = 0    # 정답

# 왼쪽 수열의 합
leftNums = {}

# 왼쪽 수열
dfs(0, N // 2, 0, 'L')

# 오른쪽 수열
dfs(N // 2, N, 0, 'R')

# 공집합 + 공집합인 경우 빼주기
if S == 0:
    ans -= 1

print(ans)
