import sys
# 공백을 추가해주어, string[0] = ' ' 이 되게 만들었다.
word1 = ' ' + sys.stdin.readline().strip()
word2 = ' ' + sys.stdin.readline().strip()

# 각 string의 길이를 저장해주고
n = len(word1)
m = len(word2)

# string의 길이만큼 2차원 배열을 만들었다. 이는 각 string의 길이일 때, LCS를 저장해두는 memo이다.
table = [[0] * m for _ in range(n)]

# memo_table[i][j]는 새롭게 추가된 string이 같으면, memo[i - 1][j - 1] + 1과 같다.
# 그렇지 않다면, word1이 한 개 짧을 때와 word2가 한 개 짧을 때 중 큰 값을 가진다.
for i in range(1, n):
    for j in range(1, m):
        if word1[i] == word2[j]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i][j - 1], table[i - 1][j])

print(table[n - 1][m - 1])