## 11726 2×n 타일링 응용문제

tile = [0, 1, 3]   # 초기값

# 현재 타일 개수 => 앞앞 * 2 + 앞
# 타일을 붙이는 방법 리스트를 생성
for idx in range(3, 1001):
    result = tile[idx-1] + (tile[idx-2] * 2)
    tile.append(result)

N = int(input())    # 입력받은 값

# 만든 리스트에서 결과 값  %  10007
print(tile[N] % 10007)