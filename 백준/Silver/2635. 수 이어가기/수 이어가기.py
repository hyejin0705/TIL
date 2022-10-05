N = int(input())

ans = 0   # 정답출력

# 입력받은 숫자보다 다음 숫자가 크면, 바로 음수 출력.
for num in range(N+1):
    lst = [N]           # 입력받은 숫자를 담은 리스트
    lst.append(num)     # 다음 숫자 리스트에 추가

    idx = 0
    while True:
        n = lst[idx] - lst[idx + 1]   # 앞 두 숫자 빼기

        if n < 0:     # 음수가 나오면 while 나가기
            break

        else:               # 양수라면,
            lst.append(n)   # 리스트에 추가
            idx += 1        # 인덱스 1 증가

    if len(lst) > ans:      # 리스트 길이가 길면,
        ans = len(lst)      # ans 갱신
        result = lst        # 리스트도 담기

print(ans)
print(*result)