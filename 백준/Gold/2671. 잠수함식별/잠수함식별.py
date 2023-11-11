def solution(string):
    i = 0
    while i < len(string):
        if i >= len(string) - 1:
            print('NOISE')
            return
        
        elif string[i:i+2] == '01':
            i += 2
            
        elif string[i:i+2] == '10':
            i += 2
            
            if string[i] == '1':
                print('NOISE')
                return
            
            while i < len(string):
                if string[i] == '1': 
                    break
                else: 
                    i += 1
                    
            else:
                print('NOISE')
                return
            
            while i < len(string) and string[i] == '1':
                if string[i] == '0': 
                    break
                else: 
                    i += 1
                    
            if i < len(string) - 1 and string[i:i+2] == '00': 
                i -= 1
            
            if string[i-1] == '0':
                print('NOISE')
                return
        
        else:
            print('NOISE')
            return
        
    print('SUBMARINE')

solution(input())