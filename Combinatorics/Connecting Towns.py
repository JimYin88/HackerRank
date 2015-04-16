if __name__ == '__main__':
    
    T = int(raw_input())
    
    for x in range(T):
        n = int(raw_input())
        s1 = list(map(int, raw_input().split()))
        print reduce(lambda a, b: a*b, s1) % 1234567
