string = input()

for i in range(len(string)):
    check = string[i:]
    if check == check[::-1]:
        break

print(len(string) + i)