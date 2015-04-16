if __name__ == '__main__':
        
    T = int(raw_input())
    
    fibo_sequence = []
    a, b = 0, 1
    
    while a <= 10**10:
        fibo_sequence.append(a)
        a, b = b, a + b
    
    for x in range(T):
        N = int(raw_input())
        if N in fibo_sequence:
            print 'IsFibo'
        else:
            print 'IsNotFibo'
