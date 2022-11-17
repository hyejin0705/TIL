s = input()
prev = ''
cnt = 0

for ck in s:
    if ck != prev:
        prev = ck
        cnt += 1

print(cnt//2)