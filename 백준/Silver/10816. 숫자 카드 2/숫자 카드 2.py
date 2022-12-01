# 디버깅: M개의 숫자카드 중에서 중복일 가능성 염두
import sys

input = sys.stdin.readline   # 시간초과 방지

N = int(input())

# 상근이 가지고 있는 숫자카드
lst = list(map(int, input().split()))

M = int(input())

# 찾아야 할 숫자카드
check = list(map(int, input().split()))

# 찾아야 할 숫자카드 dict
dic = {num: 0 for num in check}

# 상근이 카드 확인
for num in lst:
    if num in dic.keys():   # 찾아야 할 카드가 존재하면,
        dic[num] += 1       # 카운팅

for num in check:
    print(dic[num], end=' ')   # 출력하기 (공백기준)
print()