def word_check(word):
    if word == word[::-1]:
        return 1
    else:
        return 0

T = int(input())

for i in range(T):
    T_word = input()
    
    if len(T_word) >= 3 and len(T_word) <= 10:
        print(f'#{i+1} {word_check(T_word)}')

    else:
        print('단어의 길이가 잘못되었습니다.')
