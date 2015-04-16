if __name__ == '__main__':
    number_of_test = int(raw_input())
    
    for _ in range(number_of_test):        
        N = int(raw_input())
        A = list(map(int, raw_input().split()))
        
        if len(A) == 1:
            print 'YES'
        elif len(A) == 2:
            print 'NO'
        else:
            left_side, right_side = 0, sum(A[1:])
            for i in range(1, len(A)):
                left_side += A[i-1]
                right_side -= A[i]
                if left_side == right_side:
                    print 'YES'
                    break
            else:
                print 'NO'
