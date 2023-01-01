lst = list(input())

# 레이저, 열리는 인덱스, 막대 인덱스 리스트 생성.
laser_lst = []
bar = []
bar_lst = []
cnt = 0
for idx, ap in enumerate(lst):
    if ap == '(':  # 열리는 게 있으면,
        bar.append(idx)  # 위치를 저장

    else:  # 닫히는 게 나왔는데
        if lst[idx - 1] == '(':  # 앞에 열리는 게 나왔으면
            laser_lst.append(idx)  # 레이저에 저장

            bar.pop()  # 그리고 저장된 열리는 인덱스 삭제

            cnt += len(bar)  # 남은 '(' 개수 세기

        else:
            # 아니면, 열리는 인덱스 마지막 번호와, 같이 저장.
            bar_lst.append([bar[-1], idx])

            cnt += 1  # 닫히는 게 발견하면, 1증가

            bar.pop()  # 그리고 저장된 열리는 인덱스 삭제

print(cnt)