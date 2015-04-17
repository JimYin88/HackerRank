import math

def combination(n,r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

if __name__ == '__main__':
    
    T = int(raw_input())
    
    for _ in range(T):        
        N = int(raw_input())
        K = int(raw_input())
        
        print combination(N + K - 1, K) % 1000000000
