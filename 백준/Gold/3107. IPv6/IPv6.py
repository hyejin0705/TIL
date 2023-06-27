ipv6 = input()
lst = ipv6.split(':')

chk=[]
for i in lst:
    if i != '':
        chk.append(i)
        
cnt=0
total=''
for i in range(len(lst)):
    if lst[i] =='' and cnt != 1:
        total += '0000:'*(8-len(chk))
        cnt=1   
    
    elif lst[i] != '':
        if len(lst[i])<4 :
            total+= ('0'*(4-len(lst[i])))+lst[i]
            total+=":"
    
        else:
            total+=lst[i] + ":"

print(total[:-1])