import re

if __name__ == '__main__':

    N = int(raw_input())
    
    for _ in range(N):        
        string1 = raw_input()
        matchObj1 = re.search(r'^[(]([+-]?[1-9][0-9]{0,2}([.]\d{1,})?), ([+-]?[1-9][0-9]{0,2}([.]\d{1,})?)[)]$', string1)
              
        if matchObj1:
            if float(matchObj1.group(1)) < -90:
                print 'Invalid'
            elif float(matchObj1.group(1)) > 90:
                print 'Invalid'
            elif float(matchObj1.group(3)) < -180:
                print 'Invalid'
            elif float(matchObj1.group(3)) > 180:
                print 'Invalid'
            else:
                print 'Valid'
        else:
            print 'Invalid'
