# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    # len : 리스트 안의 요소들의 개수를 세주는 함수
    return sum(scores) / len(scores)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores)) # 82.5
