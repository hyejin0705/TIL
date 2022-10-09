def right(mx_idx, mx_h):
    global ans

    while c[mx_idx+1:]:
        cr = c[mx_idx+1:]
        mx = max(cr)
        mx_i = cr.index(max(cr))

        if cr[mx_i] == 0:
            break

        else:
            ans -= (mx_i + 1) * (mx_h - mx)

            mx_idx += mx_i + 1


def left(mx_idx, mx_h):
    global ans

    while c[mx_idx] > 0:
        cl = c[:mx_idx]
        mx = max(cl)
        mx_i = cl.index(max(cl))

        if cl[mx_i] == 0:
            break

        else:
            ans -= (mx_idx - mx_i) * (mx_h - mx)

            mx_idx = mx_i


N = int(input())

c = [0] * 1001

mn_i = 1001
mx_i = 0
for _ in range(N):
    idx, h = map(int, input().split())

    c[idx] = h

    mn_i = min(mn_i, idx)
    mx_i = max(mx_i, idx)

w = mx_i - mn_i + 1

mx_h = max(c)
mx_idx = c.index(max(c))

ans = w * mx_h

right(mx_idx, mx_h)

left(mx_idx, mx_h)

print(ans)