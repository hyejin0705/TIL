## sort()로 정렬하는 것보다, count 배열을 사용하는 것도 실행속도가 빠르고, 메모리를 덜 사용함.

import sys

N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())
    
    check_list[input_num] += 1    # 숫자가 나오면, count (1개 증가)
    
for i in range(10001):
    if check_list[i] > 0:               # 숫자가 존재했다면,
        for j in range(check_list[i]):  # 숫자만큼 반복해서
            print(i)                    # 출력.
            

##-------------------------------------------------------
## 메모리초과 1 - 초기 풀이방법

T = int(input())

lst = [int(input()) for _ in range(T)]

lst.sort()

print(*lst, sep='\n')


##-------------------------------------------------------
## 메모리초과 2

## 대용량의 데이터의 입출력은 sys.stdin.readline()를 사용해야 실행속도가 빠름.
## BUT 메모리초과에 대한 해답은 아니였음.ㅜㅜ

import sys

T = int(sys.stdin.readline())

lst = [int(sys.stdin.readline()) for _ in range(T)]   # 입출력의 문제보다는

lst.sort()                   # 정렬의 문제

print(*lst, sep='\n')


##-------------------------------------------------------
## 메모리초과 3
import sys

N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(sys.stdin.readline())

    check_list[input_num] = check_list[input_num] + 1

for i in range(10001):
    if check_list[i] > 0:
        num = [i] * check_list[i]      # 리스트를 하나 더 생성해서 출력하면, 메모리 초과
        print(*num, sep='\n')
        
