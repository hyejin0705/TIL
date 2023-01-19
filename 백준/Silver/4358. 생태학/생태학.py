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

tree = dict(sorted(tree_dict.items()))    # 사전순 정렬
total = sum(tree_dict.values())

for check, num in tree.items():
    print("%s %.4f" % (check, num / total * 100))  # round 활용하면 틀렸습니다 도출  >>> .f 활용


# -------------------------------------
# round 결과가 다른 이유는?

# float에 대한 round() 의 동작은 예상과 다를 수 있습니다.
# 예를 들어, round(2.675, 2) 는 2.68 대신에 2.67 을 제공합니다. 
# 이것은 버그가 아닙니다: 대부분의 십진 소수가 float로 정확히 표현될 수 없다는 사실로부터 오는 결과입니다.
