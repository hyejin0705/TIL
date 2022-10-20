find = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for t in find:
    word = word.replace(t, '*')

print(len(word))