# 1. 런타임에러(ValueError) : 1000일 때 max함수 때문에 에러 발생
# 2. 런타임에러(IndexError) : 수정했을 때, 리스트가 존재하면 반복하기를 바랬는데 :를 빼서, 요소 존재 확인만 해서 돌다가 에러발생
# 3번째 시도만에 성공!

def right(mx_idx, mx_h):      # 오른쪽 탐색
    global ans

    while c[mx_idx+1:]:       # 리스트가 존재하면, 반복 : 1000까지 숫자가 존재할 경우
        cr = c[mx_idx+1:]
        mx = max(cr)               # 오른쪽에서 최대값 확인
        mx_i = cr.index(max(cr))   # 최대값 위치 확인

        if cr[mx_i] == 0:          # 최대값이 0이면, 종료
            break

        else:
            ans -= (mx_i + 1) * (mx_h - mx)    # 위치 * 높이 차이

            mx_idx += mx_i + 1     # 최대값 위치 갱신


def left(mx_idx, mx_h):      # 왼쪽 탐색
    global ans

    while c[mx_idx] > 0:           # 값이 0이면 종료
        cl = c[:mx_idx]
        mx = max(cl)               # 왼쪽에서 최대값 확인
        mx_i = cl.index(max(cl))   # 위치 확인

        if cl[mx_i] == 0:
            break

        else:
            ans -= (mx_idx - mx_i) * (mx_h - mx)    # 최대값 위치 * 높이

            mx_idx = mx_i         # 최대값 위치 갱신


N = int(input())

c = [0] * 1001                  # 창고 리스트 생성(1 <= 창고 <= 1000)

mn_i = 1001                # 최소 인덱스(창고의 가로길이 찾기 위해)
mx_i = 0                   # 최대 인덱스(창고의 가로길이 찾기 위해)
for _ in range(N):
    idx, h = map(int, input().split())

    c[idx] = h                # 위치에 맞는 높이 넣기

    mn_i = min(mn_i, idx)     # 최소 인덱스 갱신
    mx_i = max(mx_i, idx)

w = mx_i - mn_i + 1           # 창고의 가로길이 

mx_h = max(c)               # 초기 최대값 확인
mx_idx = c.index(max(c))    # 위치 확인  (오른쪽 왼쪽 탐색을 다르게 하기 위해)

ans = w * mx_h          # 최대 창고의 넓이

right(mx_idx, mx_h)     # 오른쪽 최대높이 확인 후, 넓이 빼는 함수 호출

left(mx_idx, mx_h)

print(ans)             # 창고 넓이 출력
