if __name__ == '__main__':

    T = int(raw_input())

    for _ in range(T):
        n = int(raw_input())
        remainder = n
            
        found = False
        while found == False and remainder >= 0:
            if remainder < 0:
                break
            elif remainder % 3 == 0:
                fives = remainder
                threes = n - remainder
                found = True
            else:
                remainder -= 5
        
        if found:
            print '5'*fives + '3'*threes
        else:
            print -1
