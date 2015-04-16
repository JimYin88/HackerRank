import re

if __name__ == '__main__':

    N = int(raw_input())
    
    for i in range(N):        
        string1 = raw_input()
        match = re.search(r'^(\d{1,3})[\s-](\d{1,3})[\s-](\d{4,10})$', string1)
        print 'CountryCode=' + str(match.group(1)) + ',LocalAreaCode=' + str(match.group(2)) + ',Number=' + str(match.group(3))
