def unbounded_knapsack(w, v, c):
    m = [0]
    for r in range(1, c+1):
        val = m[r-1]
        for i, wi in enumerate(w):
            if wi > r: 
                continue
            else:
                if v[i] + m[r-wi] > val:
                    val = v[i] + m[r-wi]
        m.append(val)
    return m[c]

if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):        
        n, k = list(map(int, raw_input().split()))
        A = list(map(int, raw_input().split()))
        
        print unbounded_knapsack(A, A, k)
