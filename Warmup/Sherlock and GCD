import fractions, functools

if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):
    
        N = int(raw_input())
        A = list(map(int, raw_input().split()))
        
        gcd = functools.reduce(fractions.gcd, A)
        print('YES' if gcd == 1 else 'NO')
