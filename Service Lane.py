if __name__ == '__main__':

    N, T = list(map(int, raw_input().split()))
    width = list(map(int, raw_input().split()))
    
    for _ in range(T):        
        i, j = list(map(int, raw_input().split()))
        print min(width[i:j+1])
