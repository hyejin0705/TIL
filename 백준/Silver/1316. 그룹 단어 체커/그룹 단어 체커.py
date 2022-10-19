N = int(input())

ans = 0
for _ in range(N):
    word = input()     # 문자 출력
    word_lst = []

    for w in word:
        if w not in word_lst:     # 앞에 나왔던 문자가 아니면, 추가
            word_lst.append(w)
        else:                      # 앞에 나왔던 문자이지만,
            if w == word_lst[-1]:  # 끝에 들어온 문자와 동일하다면, 넘어가기
                continue
            else:                  # 연속적인 문자가 아니라면, 종료
                break
    else:                # for문이 종료 없이 다 돌았다면, 정답 1 증가
        ans += 1

print(ans)