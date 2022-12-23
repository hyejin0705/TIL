from collections import deque     # 시간단축 방안

def bfs(s, e):
    # q = []      # 그냥 append, pop 사용시 : 34272 KB	428 ms
    q = deque()

    q.append(s)
    v[s] = 1

    while q:
        # c = q.pop(0)
        c = q.popleft()

        if c == e:
            print(v[c] - 1)
            return

        for n in [c + 1, c - 1, c * 2]:
            if 0 <= n <= MAX and not v[n]:
                q.append(n)
                v[n] = v[c] + 1


S, E = map(int, input().split())

MAX = 100000

v = [0] * (MAX + 1)

bfs(S, E)


# # -----------------------------------------------------
# # DFS로 풀 경우, 무한 루프가 발생.

# def dfs(cnt, n):
#     global ans

#     if n == K:
#         ans = min(ans, cnt)
#         return

#     dfs(cnt + 1, n * 2)
#     dfs(cnt + 1, n + 1)
#     dfs(cnt + 1, n - 1)



# N, K = map(int, input().split())

# ans = 100000

# dfs(0, N)

# print(ans)
