if __name__ == '__main__':
    
    n, k = list(map(int, raw_input().split()))
    A = list(map(int, raw_input().split()))
    B = sorted(A, reverse=True)
    already_count = 0
    i = 0
    
    if k >= n:
        A = B
    else:
        while i < k:
            if i + already_count >= n:
                i = k
                break        
            number = B[already_count + i]
            index_a = A.index(number)
            if index_a != already_count + i:
                A[index_a], A[already_count + i] = A[already_count + i], A[index_a]
                i += 1
            else:
                already_count += 1
    
    for j in range(n):
        if j < n:
            print A[j],
        else:
            print A[j]
