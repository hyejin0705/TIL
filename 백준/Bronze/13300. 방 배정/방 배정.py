# 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000), 한 방에 배정할 수 있는 최대 인원 수 K
N, K = map(int, input().split())

# 여학생, 남학생 학년별 dict
girl = {key: 0 for key in range(1, 7)}
boy = {key: 0 for key in range(1, 7)}

for _ in range(N):
    # 학생의 성별 S와 학년 Y(1 ≤ Y ≤ 6)
    s, y = map(int, input().split())

    if s == 0:  # 성별 S는 여학생인 경우에 0
        girl[y] += 1

    else:  # 남학생인 경우에 1
        boy[y] += 1

# 방 배정
cnt = 0
if K == 1:
    cnt = N

elif K > 1:
    for year in range(1, 7):
        if girl[year] % K == 0:        # K의 배수이면,
            cnt += girl[year] / K      # K로 나눈 몫 >> 방의 개수

        else:                           # K의 배수가 아니라면,
            cnt += girl[year] // K + 1  # 인원수 // 방배정인원수 + 1

        if boy[year] % K == 0:      # 남자인 경우 위와 동일.
            cnt += boy[year] / K

        else:
            cnt += boy[year] // K + 1

print(int(cnt))