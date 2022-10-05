N = int(input())

if N >= 9 and N <= 199:
    x = input()
    x = [int(i) for i in x.split(' ')]
    if N == len(x):  
        x.sort()
        print(x[len(x)//2])      
    else:
        print('입력값이 다릅니다.')
else:
    print('값이 모자릅니다.')
