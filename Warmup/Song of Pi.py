if __name__ == '__main__':
    
    T = int(raw_input())
    
    pi_digit = '31415926535897932384626433833'
    
    for i in range(T):
        B = list(map(str, raw_input().split()))
        b = [str(len(x)) for x in B]
        b = ''.join(b)
        
        result = True
        for j in range(len(b)):
            if b[j] != pi_digit[j]:
                result = False
        if result == True:
            print "It's a pi song."
        else:
            print "It's not a pi song."
