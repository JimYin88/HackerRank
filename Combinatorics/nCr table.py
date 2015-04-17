if __name__ == '__main__':
    T = int(raw_input())
    
    for _ in range (T):
        N = int(raw_input())
        product = 1
        for i in range(N+1):
            if i == 0:
                print product % 1000000000,
            elif i < N:
                product *= (N - i + 1)
                product /= i
                print product % 1000000000,
            else:
                print 1
