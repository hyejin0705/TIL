import sys

tree_dict = {}

while True:
    string = sys.stdin.readline().strip()

    if not string:
        break

    if not tree_dict.get(string, 0):
        tree_dict.setdefault(string, 1)
    else:
        tree_dict[string] += 1

tree = sorted(list(tree_dict.keys()))
total = sum(tree_dict.values())

for check in tree:
    print("%s %.4f" % (check, tree_dict.get(check) / total * 100))