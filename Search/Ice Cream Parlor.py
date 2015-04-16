if __name__ == '__main__':
    T = int(raw_input())
    
    for t in range (T):
        M = int(raw_input())
        N = int(raw_input())
        P = map(int, raw_input().split())
        
        for i, p in enumerate(P[:-1]):
            for j in range(i+1, len(P)):
                if P[i] + P[j] == M:
                    print i + 1, j + 1
                    break
