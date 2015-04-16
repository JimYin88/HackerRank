import re

if __name__ == '__main__':

    N = int(raw_input())
    
    for _ in range(N):        
        s1 = raw_input()
        m1 = re.search(r'^(\d{1,3})[.](\d{1,3})[.](\d{1,3})[.](\d{1,3})$', s1)
        m2 = re.search(r'^[0-9a-f]{1,4}[:][0-9a-f]{1,4}[:][0-9a-f]{1,4}[:][0-9a-f]{1,4}[:][0-9a-f]{1,4}[:][0-9a-f]{1,4}[:][0-9a-f]{1,4}[:][0-9a-f]{1,4}$', s1)
              
        if m1:
            if int(m1.group(1)) < 256 and int(m1.group(2)) < 256 and int(m1.group(3)) < 256 and int(m1.group(4)) < 256:
                print 'IPv4'
            else:
                print 'Neither'            
        elif m2:
            print 'IPv6'
        else:
            print 'Neither'
