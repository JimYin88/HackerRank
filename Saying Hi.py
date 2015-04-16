import re

if __name__ == '__main__':

    N = int(raw_input())
    
    for _ in range(N):        
        string1 = raw_input()
        matchObj1 = re.search(r'^hi\s[^dD]', string1, re.I)
        
        if matchObj1:
            print string1
