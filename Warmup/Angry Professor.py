if __name__ == '__main__':
    
    T = int(raw_input())
    
    for _ in range(T):        
        N, K = list(map(int, raw_input().split()))        
        A = list(map(int, raw_input().split()))
        ontime = sum([1 for x in A if x <= 0])
        print 'YES' if ontime < K else 'NO'
