import fractions

if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range(T):
        a, b, c = list(map(int, raw_input().split()))
        print('YES' if c <= max(a, b) and c % fractions.gcd(a, b) == 0 else 'NO')
