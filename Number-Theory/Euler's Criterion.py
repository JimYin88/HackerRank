if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):
        A, M = list(map(int, raw_input().split()))
        
        if M == 2:
            print('YES')
        else:
            print('NO' if pow(A, (M - 1) // 2, M) == M - 1 else 'YES')
