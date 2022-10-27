## 그리디한 접근 방법이 필요!!

## ----------------------------------------------------------------------------------------------------------
## 첫번째, dfs() + 백트래킹을 통해 풀이  ---  런타임 에러 (RecursionError), N의 값이 클 수 있음..
## 두번째, 차이의 최대값을 0으로 만들고 sum()  -- 런타임 에러 (ValueError), N의 값이 1개일 수도 있음.

## 세번째, 두번째 방법 디버깅 -> N이 1개일 때는 그냥 0출력 -- **통과 (328 ms)**

## 최종, 리팩토링 -> N이 K보다 큰 경우만 존재한다면? sum(슬라이싱) 만으로도 풀이 가능 -- **통과 (72 ms)**

## 첫번째 런타임 에러의 이유가 재귀문제가 아니라, K가 N보다 큰 경우가 존재할 수 있다고 생각.
## 그래서 이후 풀이들을 보면, K가 클 경우를 생각해서 코드를 작성함.
## 하지만 N이 K보다 작은 경우를 생각하지 않는다면???  

##-----------------------------------------------------------------------------------------------------------

N = int(input())

K = int(input())

lst = list(map(int, input().split()))

lst.sort()

ans = []
for idx in range(N-1):
    ans.append(lst[idx + 1] - lst[idx])

# 앞뒤의 차이 리스트 생성
# [2, 3, 0, 1, 2]

# if ans:                                # 세번째 방법
#     for _ in range(K-1):
#         ans[ans.index(max(ans))] = 0
#
#         if sum(ans) == 0:
#             break

# print(sum(ans))

ans.sort()

print(sum(ans[:N-K]))             # 리팩토링!


## -----------------------------------------------------
## 첫번째, dfs() + 백트래킹을 통해 풀이  ---  런타임 에러 (RecursionError), N의 값이 클 수 있음..
# def dfs(n, cnt, sm):
#     global mn

#     if sm >= mn:         # 백트래킹 : 가지치기
#         return

#     if n == N-1:          # len(차이값 리스트) == N - 1
#         if cnt == N - K:      # 요소의 개수 == len(ans) - (K - 1)  == 전체 - 기준점
#             mn = min(mn, sm)  # 최소값 갱신
#         return

#     dfs(n+1, cnt + 1, sm + ans[n])   # 요소를 포함했을 때,
#     dfs(n+1, cnt, sm)                # 포함하지 않았을 때,

# N = int(input())

# K = int(input())

# lst = list(map(int, input().split()))

# lst.sort()   # 센서들의 위치를 정렬하기

# ans = []
# for idx in range(N-1):
#     ans.append(lst[idx+1] - lst[idx])

# # 앞뒤의 차이 리스트 생성
# # [2, 3, 0, 1, 2]

# mn = 10e9
# dfs(0, 0, 0)    # dfs 돌리기

# print(mn)


## 두번째, 차이의 최대값을 0으로 만들고 sum()  -- 런타임 에러 (ValueError), N의 값이 1개일 수도 있음.
# N = int(input())

# K = int(input())

# lst = list(map(int, input().split()))

# lst.sort()

# ans = []
# for idx in range(N-1):
#     ans.append(lst[idx + 1] - lst[idx])

# # 앞뒤의 차이 리스트 생성
# # [2, 3, 0, 1, 2]

# for _ in range(K-1):
#     ans[ans.index(max(ans))] = 0

#     if sum(ans) == 0:
#         break

# ans.sort()

# print(sum(ans[:N-K]))
