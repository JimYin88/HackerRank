import re

if __name__ == '__main__':

    N = int(raw_input())
    
    count = 0
    for _ in range(N):        
        string1 = raw_input()
        matchObj = re.search(r'hackerrank', string1, re.I)

        if matchObj:
            count += 1
    
    print count
