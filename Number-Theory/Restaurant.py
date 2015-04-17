def gcd(a, b): 
    return b and gcd(b, a % b) or a

if __name__ == '__main__': 
    T = int(raw_input()) 
     
    for _ in range(T): 
        l, b = list(map(int, raw_input().split())) 
        print(l * b // gcd(l, b)**2)
