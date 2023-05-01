n,m = map(int,input().split())
 
#dp값은 최소 몇학기 인지
dp = [1] * (n)
 
#인덱스번호가 과목번호, 안에 든 값들은 선수과목 번호
array = [[]for i in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    array[b-1].append(a)
 
for i in range(0,n):
    #선수과목이 없는 빈리스트라면 dp값을 1로
    if array[i] == False:
        continue
    #선수과목이 있다면 전부 dp해보기
    else:
        for j in range(len(array[i])):
            dp[i] = max(dp[array[i][j]-1]+1, dp[i])
print(*dp)