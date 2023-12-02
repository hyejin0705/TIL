import sys

goal = int(sys.stdin.readline())

def test(n):
    if n == 1:
        print(2)
    else:
        ans = 0; aux = 0;
        ans_2 = 1; ans_1 = 2;
        aux_1 = 1;
        for i in range(n-1):
            aux = (ans_1 + aux_1) % 1000000007
            ans = (aux_1 + ans_2 + ans_1 + aux) % 1000000007
            ans_2, ans_1, aux_1 = (ans_1, ans, aux)
        print(ans)

test(goal)