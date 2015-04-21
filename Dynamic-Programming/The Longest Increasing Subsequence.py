def basic_lis(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] < val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)

if __name__ == '__main__':
    N = int(raw_input())
    
    A = []
    for _ in range(N):        
        A.append(int(raw_input()))
    print basic_lis(A)
