if __name__ == '__main__':
    
    N, M = list(map(int, raw_input().split()))
    
    result = [0] * N
    
    for _ in range(M):        
        a, b, k = list(map(int, raw_input().split()))
        for i in range(a - 1, b):
            result[i] += k
        
    print max(result)
