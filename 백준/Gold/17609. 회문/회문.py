N = int(input())

def is_palindrome(check):
    i, j = 0, len(check) - 1
    while i < j:
        if check[i] == check[j]:
            i += 1
            j -= 1

        else:
            if check[i + 1] == check[j]:
                temp = check[i + 1 : j + 1]
                if temp == temp[::-1]:
                    return 1

            if check[i] == check[j - 1]:
                temp = check[i: j]
                if temp == temp[::-1]:
                    return 1

            return 2

    return 0


for _ in range(N):
    print(is_palindrome(input()))