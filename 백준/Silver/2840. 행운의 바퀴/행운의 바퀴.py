N, K = map(int, input().split())

lst = [input().split() for _ in range(K)]

target = lst[-1][1]   # 마지막 글자 저장

cnt = ['?'] * N    # 초기값을 ?로 하기
idx = 0

for num, alpha in lst:
    idx += int(num)     # 글자 회전 수 누적합

    i = idx % N         # 누적합 / N의 나머지로 인덱스 확인.

    if cnt[i] == '?':      # 아무것도 없다면,
        cnt[i] = alpha     # 글자 적음

        # 적고 나서, 글자가 2개 이상 존재하다면,
        if cnt.count(cnt[i]) >= 2:
            cnt = '!'               # 추측 실패.
            break

    elif cnt[i] != alpha:     # 다른 글자가 적혀 있다면,
        cnt = '!'               # 추측 실패.
        break

else:
    while len(cnt) >= 2:     # 길이가 2개 이상이면,
        n = cnt.pop(0)       # 처음에서 빼서
        cnt.append(n)        # 뒤로 넣기
        if n == target:      # 만약 목표 글자가 나오면, 종료
            break

print(''.join(cnt[::-1]))    # 뒤에서부터 출력
