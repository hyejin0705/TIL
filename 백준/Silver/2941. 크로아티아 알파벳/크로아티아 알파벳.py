## 문제를 단순하게 생각하자?

find = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for t in find:
    word = word.replace(t, '*')   # replace를 통해서 찾고 한 글자로 변경

print(len(word))



## ---------------------------------------------------------
## 이전 풀이 >>> 런타임에러 발생 왜?
## 메모리 문제? 아니면 while를 종료하지 못하는 경우가 있었나?
## 대회문제라서 테케 확인할 예정.
## ----------------------------------------------------------------------------
# 2글자 문자로 일단 통일하기 위해 dz= 를  dz로 저장
# find = ['c=', 'c-', 'dz', 'd-', 'lj', 'nj', 's=', 'z=']

# word = input()
# N = len(word)

# idx = ans = 0
# while idx < N:
#     check = word[idx: idx + 2]
#     if check in find:              # 찾는 글자에 존재하는지 확인
#         if check == 'dz':          # dz를 찾으면
#             if word[idx+2] == '=': # 뒤에 =이 있는지 확인
#                 ans += 1           
#                 idx += 3           # 있다면, 인덱스 3글자 뒤부터, 정답 count
#             else:
#                 ans += 1
#                 idx += 1           # 없다면, 인덱스 1글자 뒤부터
#         else:                 # 다른 찾는 문자였다면,
#             ans += 1          
#             idx += 2          # 2글자 뒤부터 시작, 정답 count
    
#     else:              # 찾는 글자가 아니라면,
#         ans += 1
#         idx += 1       # 1글자 뒤부터 시작

# print(ans)
