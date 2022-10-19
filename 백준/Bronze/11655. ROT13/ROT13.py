word = list(input())

ans = ''
for w in word:
    if w.isalpha():       # 알파벳이면, 13글자 밀어서 출력
        num = ord(w) + 13  
        # ord(): 문자 -> 숫자

        # 알파벳 대문자: 65 ~ 90  (아스키 코드)
        # 소문자: 97 ~ 122  (아스키 코드)
        if (w.isupper() and num > 90) or (w.islower() and num > 122):
            num -= 26

        ans += chr(num)    # chr(): 숫자 -> 문자

    else:         # 공백이나, 숫자라면,
        ans += w  # 그냥 출력

print(ans)