if __name__ == '__main__':
    N, K = list(map(int, (raw_input().split())))
    n_array = sorted(list(map(int, (raw_input().split()))))
    
    first = 0
    second = 1
    count = 0
    
    while second < N:
        if n_array[second] - n_array[first] == K:
            count += 1
            second += 1
        elif n_array[second] - n_array[first] < K:
            second += 1
        else:
            if second - first == 1:
                second += 1
            else:
                first += 1
                
    print count
