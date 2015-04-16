import re

if __name__ == '__main__':

    N = int(raw_input())
    
    for _ in range(N):        
        string1 = raw_input()
        matchObj1 = re.search(r'^hackerrank', string1, re.I)
        matchObj2 = re.search(r'hackerrank$', string1, re.I)

        if matchObj1 and matchObj2:
            print 0
        elif matchObj1:
            print 1
        elif matchObj2:
            print 2
        else:
            print -1
