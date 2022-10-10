A, B = map(int, input().split())

num = 2
gcd = 1
while A >= num and B >= num:
    if A % num == 0 and B % num == 0:
        gcd *= num
        A /= num
        B /= num
    
    else:
        num += 1

lcm = gcd * A * B
       
print(gcd)
print(int(lcm))