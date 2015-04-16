import re

if __name__ == '__main__':

    N = int(raw_input())
    
    count = 0
    for _ in range(N):        
        string1 = raw_input()
        matchObj = re.search(r'^[A-Z]{5}[0-9]{4}[A-Z]$', string1)

        if matchObj:
            print 'YES'
        else:
            print 'NO'
