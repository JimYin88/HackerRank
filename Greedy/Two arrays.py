if __name__ == '__main__':
    
    T = int(raw_input())
    
    for _ in range(T):
        n, k = list(map(int, raw_input().split()))
        A = sorted(list(map(int, raw_input().split())))
        B = sorted(list(map(int, raw_input().split())), reverse=True)
    
        result = 'YES'
        for i in range(n):
            if A[i] + B[i] < k:
                result = 'NO'
        
        print result
