if __name__ == '__main__':
    
    T = int(raw_input())
    
    for _ in range(T):        
        N = int(raw_input())
        A = sorted(list(map(int, raw_input().split())), reverse=True)
        
        result = 1
        for i in range(N):
            if N - A[i] <= 0:
                result = 0
            else:
                result *= (N - A[i] - i)
        
        print result % 1000000007
