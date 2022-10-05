def inorder(n):    # 중위순회
    global ans

    if n:
        inorder(ch1[n])     # 왼쪽부터
        ans += string[n]    # 중간은 문자열에 붙이기
        inorder(ch2[n])     # 오른쪽


T = 10
for test_case in range(1, T + 1):
    N = int(input())

    ch1 = [0] * (N + 1)   # 왼
    ch2 = [0] * (N + 1)   # 오

    string = [0] * (N + 1)   # 문자열 리스트

    for _ in range(N):

        # 부모노드, 문자, 자식노드
        p, alpha, *lst = input().split()

        string[int(p)] = alpha   # 문자 추가

        if lst:                  # 자식노드가 존재하고
            if len(lst) == 2:             # 개수가 2개라면
                ch1[int(p)] = int(lst[0]) # 처음은 왼
                ch2[int(p)] = int(lst[1]) # 두번째는 오
            else:
                ch1[int(p)] = int(lst[0]) # 자식노드가 1개라면, 왼

    ans = ''      # 문자열

    inorder(1)    # 중위순회

    print(f'#{test_case} {ans}')