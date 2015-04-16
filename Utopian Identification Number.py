import re

if __name__ == '__main__':
    
    N = int(raw_input())
    
    for _ in range(N):
        identification = raw_input()
        matchObj = re.match( r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}', identification)
        if matchObj:
            print 'VALID'
        else:
            print 'INVALID'
