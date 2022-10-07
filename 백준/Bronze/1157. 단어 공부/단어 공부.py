word = list(input().upper())  # 대소문자 구분X : 대문자로 변경.

letter = list(set(word))  # set : 중복제거

cnt = [0] * len(letter)   # 빈도수, 카운팅 리스트

for idx, l in enumerate(letter):
    cnt[idx] = word.count(l)

if cnt.count(max(cnt)) >= 2:   # 최대 빈도수가 여러 개면 ? 출력
    result = '?'
else:
    idx = cnt.index(max(cnt))  # index : 최대빈도수 위치 확인
    result = letter[idx]       # 단어찾기

print(result)