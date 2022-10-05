string = input()

for idx in range(0, len(string), 10):
    print(string[idx:idx + 10])