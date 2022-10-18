# 문제의 요점: EOF를 어떻게 찾느냐?
#            문제에서 끝나는 지점을 알려주지 않음.
#            EOF지점을 찾아서 끝내줘야 하는 문제!

while True:
    try:
        print(input())
    except EOFError:    # try ~ except문을 활용하여 에러가 발생하면 끝나는 걸로 작성.
        break