import sys

read = sys.stdin.readline

def change_zero(light):
    count = 1
    light[0] = not light[0]
    light[1] = not light[1]

    for i in range(1, len(light)):
        if light[i-1] == hope[i-1]:
            continue
        else:
            count += 1

            light[i-1] = not light[i-1]
            light[i] = not light[i]

            if i < len(light)-1:
                light[i+1] = not light[i+1]

    if hope == light:
        return count
    return 200002

def non_change_zero(light):
    count = 0

    for i in range(1, len(light)):
        if light[i-1] == hope[i-1]:
            continue
        else:
            count += 1

            light[i-1] = not light[i-1]
            light[i] = not light[i]

            if i < len(light)-1:
                light[i+1] = not light[i+1]

    if hope == light:
        return count

    return 100002

N = int(read().rstrip("\n"))

state = list(map(int, read().rstrip("\n")))
hope = list(map(int, read().rstrip("\n")))

count1 = change_zero(state[:])
count2 = non_change_zero(state[:])

answer = min(count1, count2)

if answer == 100002:
    answer = -1

print(answer)