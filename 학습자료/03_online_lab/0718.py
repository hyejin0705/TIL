
score = {'python':80,'django':89, 'web': 83}

# 1. algorithm = 90
score['algorithm'] = 90

# 2. python 과목 점수 수정
score['python'] = 85
# score.update({'python': 85})

# 3. 전체 과목 평균 점수를 구해라
# print(score.values())
print( sum(score.values()) / len(score.values()) )

