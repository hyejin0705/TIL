N = input()
ans = 0
while N:
    if int(N) == 1:    # 1이면, 끝
        ans += 1
        break

    if N.count('1'):           # 1의 존재 여부 파악
        idx = N.index('1')       # 1이 존재하면, 위치 파악
        N = N[:idx] + N[idx+1:]   # 1 빼기
        if not int(N):            # 1를 뺐는데, 0이라면, 종료
            ans += 1
            break
    else:
        N = str(int(N) - 1)      # 빼고 다시 문자열로 변환
    ans += 1    # 전체적으로 한바퀴 돌았다면, 1회 실행

print(ans)
