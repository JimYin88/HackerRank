import re

if __name__ == '__main__':

    N = int(raw_input())
    
    for _ in range(N):        
        string1 = raw_input()
        matchObj1 = re.search(r'^[_.]\d+[A-Za-z]*[_]?$', string1)
       
        if matchObj1:
            print 'VALID'
        else:
            print 'INVALID'
