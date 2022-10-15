T = int(input())

for _ in range(T):
    string = input().split()
    
    for word in string:
        print(word[::-1], end = ' ')
    print()